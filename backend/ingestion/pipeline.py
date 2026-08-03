from backend.database.repository_chunks import insert_chunks
from backend.ingestion.chunk import split_text_into_chunks
from backend.ingestion.extract import extract_text_from_pdf


def index_document(document_id: str, file_path: str) -> int:
    """Extraction and indexing of a PDF document into database."""

    pages = extract_text_from_pdf(file_path)

    chunks = split_text_into_chunks(document_id, pages)

    return insert_chunks(chunks)
