import logging

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.models.base import Base
from app.settings import settings

log = logging.getLogger(__name__)


class PostgresEngine:
    def __init__(self) -> None:
        self.engine = None
        self.async_session = None

    async def connect_to_engine(self):
        if self.engine:
            raise ValueError('Engine already exists')
        self.engine = create_async_engine(
            url=f'postgresql+asyncpg://csgo_user:csgo_password@csgo_postgres:5432/csgo_database',
            echo=False,
            echo_pool=False,
            pool_size=settings.postgres.pool_size,
            max_overflow=settings.postgres.max_overflow,
        )
        self.async_session = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
        )

    async def create_tables(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def drop_tables(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
