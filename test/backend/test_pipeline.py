from backend.ingestion.pipeline import index_document

import uuid
from pathlib import Path

def test_index_document():
    document_id = str(uuid.uuid4())
    file_path = Path(__file__).parent / "test_extract.pdf"
    metadata = {"author": "John Doe", "topic":"law"}

    nb_chunk = index_document(document_id, file_path)

    