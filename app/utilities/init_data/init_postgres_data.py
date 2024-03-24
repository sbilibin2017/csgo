import json
import os
from typing import Generator, NoReturn
from datetime import datetime
from dateutil.parser import parse
from sqlalchemy.dialects.postgresql import insert
from app.engines import PostgresEngine
from app.models import (
    GameDB,
    MapDB,
    PlayerDB,
    RoundDB,
    StatisticDB,
    TeamDB,
    TeamPlayerDB,
)


PATH_TO_GAMES = './app/data/games'


def _extract_game_data() -> Generator:
    for fnm in os.listdir(PATH_TO_GAMES):
        pth = os.path.join(PATH_TO_GAMES, fnm)
        with open(pth, 'r') as f:
            raw = json.load(f)

        map = {}
        map['map_id'] = raw['map']['id']
        map['name'] = raw['map']['name'] or 'default'
        map = [map]

        teams, players, team_players = [], [], []
        for player in raw['players']:
            t = {
                'team_id': player['team']['id'],
                'name': player['team']['name'] or 'default',
                'location': player['team']['location'] or 'default',
            }
            if t not in teams:
                teams.append(t)
            players.append(
                {
                    'player_id': player['player']['id'],
                    'name': player['player']['name'] or 'default',
                    'nationality': player['player']['nationality']
                    or 'default',
                }
            )

            team_players.append(
                {
                    'game_id': raw['id'],
                    'team_id': player['team']['id'],
                    'player_id': player['player']['id'],
                }
            )
        begin_at = parse(raw['begin_at'])
        game = {}
        game['game_id'] = raw['id']
        game['begin_at'] = datetime(
            year=begin_at.year,
            month=begin_at.month,
            day=begin_at.day,
            hour=begin_at.hour,
            tzinfo=None,
        )
        game['map_id'] = raw['map']['id']
        game = [game]

        stats = []
        for player in raw['players']:
            d = {}
            d['game_id'] = raw['id']
            d['player_id'] = player['player']['id']
            for key in [
                'assists',
                'deaths',
                'first_kills_diff',
                'flash_assists',
                'headshots',
                'k_d_diff',
                'kills',
            ]:
                d[key] = player[key] or 0
            for key in ['adr', 'kast', 'rating']:
                d[key] = player[key] or 0.0
            stats.append(d)

        rounds = []
        for rnd in raw['rounds']:
            d = {}
            d['game_id'] = int(raw['id'])
            d['ct_id'] = rnd['ct']
            d['t_id'] = rnd['terrorists']
            d['winner_id'] = rnd['winner_team']
            d['round'] = rnd['round']
            d['outcome'] = rnd['outcome']
            if (
                (d['ct_id'] is not None)
                & (d['t_id'] is not None)
                & (d['winner_id'] is not None)
                & (d['outcome'] is not None)
            ):
                if d['winner_id'] in [d['ct_id'], d['ct_id']]:
                    rounds.append(d)
        yield (map, teams, players, game, team_players, stats, rounds)


async def _load_game_data(
    maps: list[dict],
    teams: list[dict],
    players: list[dict],
    games: list[dict],
    team_players: list[dict],
    stats: list[dict],
    rounds: list[dict],
) -> NoReturn:
    engine = PostgresEngine()
    await engine.connect_to_engine()
    async with engine.engine.connect() as conn:
        await conn.execute(insert(MapDB).on_conflict_do_nothing(), maps)
        await conn.commit()

        await conn.execute(insert(TeamDB).on_conflict_do_nothing(), teams)
        await conn.commit()

        await conn.execute(insert(PlayerDB).on_conflict_do_nothing(), players)
        await conn.commit()

        await conn.execute(insert(GameDB).on_conflict_do_nothing(), games)
        await conn.commit()

        await conn.execute(insert(TeamPlayerDB), team_players)
        await conn.commit()

        await conn.execute(insert(StatisticDB), stats)
        await conn.commit()

        await conn.execute(insert(RoundDB), rounds)
        await conn.commit()
    del engine


async def init_postgres_data():
    for (
        maps,
        teams,
        players,
        games,
        team_players,
        statistics,
        rounds,
    ) in _extract_game_data():
        await _load_game_data(
            maps, teams, players, games, team_players, statistics, rounds
        )
