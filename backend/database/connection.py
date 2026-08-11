import logging
from collections.abc import Generator
from contextlib import contextmanager


from psycopg import Connection
from psycopg_pool import ConnectionPool

from backend.config import get_database_settings

logger = logging.getLogger(__name__)

_pool: ConnectionPool | None = None


def get_pool() -> ConnectionPool:
    global _pool

    if _pool is None:
        pool = ConnectionPool(
            get_database_settings().conninfo,
            min_size=1,
            max_size=10,
            open=False,
            check=ConnectionPool.check_connection,
            name="ask_your_data",
        )
        pool.open()
        pool.wait(timeout=5)

        logger.info(
            "Connection settings: host = %s / port = %s / dbname = %s",
            get_database_settings().host,
            get_database_settings().port,
            get_database_settings().dbname,
        )

        _pool = pool

    return _pool


@contextmanager
def get_connection() -> Generator[Connection]:
    with get_pool().connection() as conn:
        yield conn


def close_pool() -> None:
    global _pool

    if _pool is not None:
        _pool.close()
        _pool = None
