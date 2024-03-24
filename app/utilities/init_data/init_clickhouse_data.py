import json
import os
from typing import NoReturn

from asynch.cursors import DictCursor

from app.engines import ClickhouseEngine

PATH_TO_PROFILES = './app/data/profiles'


async def init_clickhouse_data() -> NoReturn:
    engine = ClickhouseEngine()
    await engine.connect_to_engine()
    columns = ', '.join(
        [
            'game_id',
            'begin_at',
            'timestamp',
            'year',
            'month',
            'day',
            'weekday',
            'hour',
            'map_id',
            'team_id',
            'player_id',
            'team_opponent_id',
            'player_opponent_id',
            'adr',
            'assists',
            'deaths',
            'first_kills_diff',
            'flash_assists',
            'headshots',
            'k_d_diff',
            'kast',
            'kills',
            'rating',
            'start_ct',
            'total_rounds',
            'win',
            'r1_win',
            'r2_win',
            'r16_win',
            'r17_win',
            'h1_win_round_count',
            'h2_win_round_count',
            'h1_eliminated_count',
            'h1_exploded_count',
            'h1_defused_count',
            'h1_timeout_count',
            'h2_eliminated_count',
            'h2_exploded_count',
            'h2_defused_count',
            'h2_timeout_count',
        ]
    )
    for fnm in os.listdir(PATH_TO_PROFILES):
        pth = os.path.join(PATH_TO_PROFILES, fnm)
        with open(pth, 'r') as f:
            profiles = json.load(f)
        async with engine.engine.cursor(cursor=DictCursor) as cursor:
            await cursor.execute(
                f'INSERT INTO csgo_database.profile({columns}) VALUES',
                profiles,
            )
    del engine
