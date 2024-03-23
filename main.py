from fastapi import FastAPI

from app.api.v1 import router as api_v1_router
from app.app import configure_di_container, create_app

app: FastAPI = create_app(
    title='CSGO api',
    version='1.0.0',
    lifespan=configure_di_container,
    routers=(api_v1_router,),
)
