import uuid
from collections.abc import Generator

import pytest
from alembic import command
from alembic.config import Config
from dotenv import load_dotenv
from psycopg import sql

from backend.config import PROJECT_ROOT, get_database_settings
from backend.database.connection import close_pool, get_connection
from backend.database.repository_document import insert_document

load_dotenv(PROJECT_ROOT / "test" / ".env_test", override=True)
get_database_settings.cache_clear()


def assert_test_database() -> None:
    """Abort the whole session unless the configured database is a test database."""
    dbname = get_database_settings().dbname
    if not dbname.endswith("_test"):
        pytest.exit(
            f"Rejecting to migrate / empty the database '{dbname}' : "
            "its name need to end with '_test'.",
            returncode=1,
        )


def alembic_config() -> Config:
    return Config(PROJECT_ROOT / "alembic.ini")


def run_migrations() -> None:
    """Bring the test database up to the latest Alembic's revision tracker."""
    command.upgrade(alembic_config(), "head")


def truncate_all_tables() -> None:
    """Empty every table of the public schema, except Alembic's revision tracker."""
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(
            """
            SELECT tablename
            FROM pg_tables
            WHERE schemaname = 'public' AND tablename <> 'alembic_version'
            """
        )
        tables = [row[0] for row in cur.fetchall()]

        if not tables:
            return

        cur.execute(
            sql.SQL("TRUNCATE {} CASCADE").format(
                sql.SQL(", ").join(sql.Identifier(t) for t in tables)
            )
        )


@pytest.fixture(scope="session", autouse=True)
def initialize_test_database() -> Generator[None, None, None]:
    assert_test_database()
    run_migrations()

    yield

    close_pool()


@pytest.fixture(autouse=True)
def clean_database() -> None:
    """Give every test a blank slate, before it runs."""
    truncate_all_tables()


@pytest.fixture
def document_id(clean_database: None) -> str:
    document_id = str(uuid.uuid4())

    insert_document(
        document_id,
        filename="test_document.pdf",
        file_path="/path/to/test_doc.txt",
        metadata={"author": "John Doe"},
    )

    return document_id
