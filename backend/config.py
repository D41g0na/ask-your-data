from functools import lru_cache
from pathlib import Path
from urllib.parse import quote_plus

from psycopg.conninfo import make_conninfo
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_ignore_empty=True,
        env_prefix="POSTGRES_",
        extra="ignore",
        frozen=True,
    )

    host: str
    port: int = 5432
    dbname: str = Field(validation_alias="POSTGRES_DB")
    user: str
    password: SecretStr

    @property
    def conninfo(self) -> str:
        return make_conninfo(
            host=self.host,
            port=self.port,
            dbname=self.dbname,
            user=self.user,
            password=self.password.get_secret_value(),
        )

    @property
    def sqlalchemy_url(self) -> str:
        """Return a DSN SQLAlchemy for Alembic, value may contain password in clear, but never log it or print it."""
        return f"postgresql+psycopg://{quote_plus(self.user)}:{quote_plus(self.password.get_secret_value())}@{self.host}:{self.port}/{self.dbname}"


@lru_cache(maxsize=1)
def get_database_settings() -> DatabaseSettings:
    return DatabaseSettings()  # type: ignore[call-arg]
