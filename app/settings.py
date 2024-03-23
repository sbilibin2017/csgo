from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    develop: bool = False
    host: str = '127.0.0.1'
    port: int = 8900
    title: str = 'API'
    version: str = 'v1.0'
    doc_url: str = '/docs'
    openapi_url: str = '/openapi.json'
    log_level: str = 'debug'
    search_limit_size: int = 25
    workers: int = 1
    pagination_page: int = 1
    pagination_page_size: int = 25


class PostgresSettings(BaseSettings):
    user: str = 'csgo_user'
    password: str = 'csgo_password'
    database: str = 'csgo_database'
    host: str = 'localhost'
    port: int = 5432
    pool_size: int = 20
    max_overflow: int = 5


class ClickhouseSettings(BaseSettings):
    host: str = 'localhost'
    user: str = 'csgo_user'
    password: str = 'csgo_password'
    port: int = 9000
    database: str = 'csgo_database'


class JWTSettings(BaseSettings):
    expires: int = 60
    secret: str = 'GrandmaLivedWithTwoCheerfulGeeseOneGrayAndTheOtherWhiteTwoCheerfulGeese.'
    algorythm: str = 'HS256'


class DockerSettings(BaseSettings):
    postgres_host: str = 'postgres'
    clickhouse_host: str = 'clickhouse'


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    postgres: PostgresSettings = PostgresSettings()
    clickhouse: ClickhouseSettings = ClickhouseSettings()
    jwt: JWTSettings = JWTSettings()
    docker: DockerSettings = DockerSettings()


settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8',
)
