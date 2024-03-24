from app.utilities.init_data.init_clickhouse_data import init_clickhouse_data
from app.utilities.init_data.init_postgres_data import init_postgres_data

__all__ = [
    'init_postgres_data',
    'init_clickhouse_data',
]
