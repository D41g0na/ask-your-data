from backend.database.repository_chunks import insert_chunks
from backend.ingestion.chunk import split_text_into_chunks
from backend.ingestion.extract import extract_text_from_pdf

import logging

logger = logging.getLogger(__name__)


def index_document(document_id: str, file_path: str) -> int:
    """Extraction and indexing of a PDF document into database."""

    logger.info("Indexing document_id=%s from %s", document_id, file_path)

    pages = extract_text_from_pdf(file_path)
    chunks = split_text_into_chunks(document_id, pages)
    inserted = insert_chunks(chunks)

    logger.info("Indexed document_id=%s: %s chunks inserted", document_id, inserted)

    return inserted
