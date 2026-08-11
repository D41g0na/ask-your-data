import uuid

from backend.database.connection import get_connection
from backend.database.repository_chunks import insert_chunks
from backend.database.repository_document import insert_document


def test_insert_document(created_documents):
    document_id = str(uuid.uuid4())
    created_documents.append(document_id)

    rows_inserted = insert_document(
        document_id,
        "test_doc.txt",
        "/path/to/test_doc.txt",
        {"author": "John Doe", "pages": 10},
    )

    assert rows_inserted == 1


def test_insert_chunks(document_id):
    chunks = [
        {
            "chunk_id": str(uuid.uuid4()),
            "document_id": document_id,
            "chunk_index": i,
            "page_start": 1,
            "page_end": 1,
            "content": f"Test chunk{i}",
            "language": "fr",
        }
        for i in range(3)
    ]

    assert insert_chunks(chunks) == 3

    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(
            "SELECT COUNT(*) FROM chunks WHERE document_id = %s", (document_id,)
        )
        assert cur.fetchone()[0] == 3


def test_insert_chunks_empty():
    assert insert_chunks([]) == 0
