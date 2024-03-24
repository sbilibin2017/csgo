from __future__ import annotations

import os
from typing import NoReturn

from asynch import connect
from asynch.connection import Connection
from asynch.cursors import DictCursor

PATH_TO_MIGRATIONS_DIR = './app/migrations/clickhouse'


class ClickhouseEngine:
    def __init__(self):
        self.engine: Connection | None = None

    async def connect_to_engine(self) -> NoReturn:
        if self.engine:
            raise ValueError('Engine already exists')
        self.engine = await connect(
            host='csgo_clickhouse',
            user='csgo_user',
            password='csgo_password',
            port=9000,
            database='csgo_database',
        )

    async def disconnect_from_engine(self) -> NoReturn:
        await self.engine.close()

    async def create_tables(self) -> NoReturn:
        for fnm in os.listdir(PATH_TO_MIGRATIONS_DIR):
            pth = os.path.join(PATH_TO_MIGRATIONS_DIR, fnm)
            with open(pth, 'r') as f:
                query = f.read()
            async with self.engine.cursor(cursor=DictCursor) as cursor:
                await cursor.execute(query)

    async def drop_tables(self) -> NoReturn:
        async with self.engine.cursor(cursor=DictCursor) as cursor:
            await cursor.execute('SHOW TABLES FROM csgo_database')
            for row in await cursor.fetchall():
                await cursor.execute(f"DROP TABLE csgo_database.{row['name']}")
