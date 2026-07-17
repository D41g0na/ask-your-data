import uuid

import pytest

from backend.database.repository_document import insert_document
from backend.database.connection import get_connection
from backend.database.schema import (
    create_documents_table,
    create_chunks_table,
)


@pytest.fixture(scope="session", autouse=True)
def initialize_test_database():
    create_documents_table()
    create_chunks_table()

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

    conn = get_connection()

    try:
            with conn.cursor() as cur:
                cur.execute(
                    " DELETE FROM documents WHERE document_id = %s",
                    (document_id,),
                )
            conn.commit()

    finally:
        conn.close()