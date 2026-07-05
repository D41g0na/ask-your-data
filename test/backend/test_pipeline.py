from backend.ingestion.pipeline import index_document

import uuid

def test_index_document():
    document_id = str(uuid.uuid4())
    file_path = "/test/backend/test_extract.pdf"
    metadata = {"author": "John Doe", "topic":"law"}

    nb_chunk = index_document(document_id, file_path)

    