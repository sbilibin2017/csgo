from contextlib import asynccontextmanager
from typing import Coroutine

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from rodi import Container

from app import dependencies
from app.engines.clickhouse import ClickhouseEngine
from app.engines.postgres import PostgresEngine
from app.settings import settings

# from app.init_data import InitData


@asynccontextmanager
async def configure_di_container(app: FastAPI):  # noqa
    dependencies.container = Container()
    dependencies.container.register(obj_type=ClickhouseEngine, instance=ClickhouseEngine())
    dependencies.container.register(obj_type=PostgresEngine, instance=PostgresEngine())

    db: PostgresEngine = dependencies.container.resolve(PostgresEngine)
    await db.connect_to_engine()
    await db.create_tables()
    # await load_data_postgres()

    db: ClickhouseEngine = dependencies.container.resolve(ClickhouseEngine)
    await db.connect_to_engine()
    await db.create_tables()
    # await load_data_clickhouse()

    yield


def create_app(
    title: str,
    version: str,
    lifespan: Coroutine | None,
    routers: list[APIRouter],
) -> FastAPI:
    app = FastAPI(
        title=title,
        version=version,
        docs_url=settings.app.doc_url,
        openapi_url=settings.app.openapi_url,
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    for router in routers:
        app.include_router(router)

    return app
