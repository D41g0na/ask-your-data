import uuid

from backend.database.repository_chunks import insert_chunk
from backend.database.repository_document import insert_document


def test_insert_document():
    document_id = str(uuid.uuid4())
    filename = "test_doc.txt"
    file_path = "/path/to/test_doc.txt"
    metadata = {"author": "John Doe", "pages": 10}

    inserted_id = insert_document(document_id, filename, file_path, metadata)

    assert inserted_id == document_id
    assert isinstance(inserted_id, str)
    assert inserted_id is not None


def test_insert_chunk(document_id):
    chunk_id = str(uuid.uuid4())

    inserted_id = insert_chunk(
        chunk_id=chunk_id,
        document_id=document_id,
        chunk_index=0,
        page_start=1,
        page_end=1,
        content="This is a test chunk of text.",
        metadata={"author": "John Doe", "pages": 10},
    )

    assert inserted_id == chunk_id
    assert isinstance(inserted_id, str)
    assert document_id is not None
