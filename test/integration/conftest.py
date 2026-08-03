import uuid

import pytest

from backend.database.connection import get_connection
from backend.database.repository_document import insert_document
from backend.database.schema import create_chunks_table, create_documents_table


@pytest.fixture(scope="session", autouse=True)
def initialize_test_database():
    create_documents_table()
    create_chunks_table()

    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(
            "TRUNCATE documents CASCADE;"
        )


@pytest.fixture
def document_id():
    document_id = str(uuid.uuid4())

    insert_document(
        document_id,
        filename="test_document.pdf",
        file_path="/path/to/test_doc.txt",
        metadata={"author": "John Doe"},
    )

    yield document_id


    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(
            " DELETE FROM documents WHERE document_id = %s",
            (document_id,),
        )

@pytest.fixture
def created_documents():
    ids = []

    yield ids

    with get_connection() as conn, conn.cursor() as cur:
        cur.executemany(
            " DELETE FROM documents WHERE document_id = %s",
            [(i,) for i in ids]
        )