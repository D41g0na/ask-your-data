from backend.ingestion.extract import extract_text_from_pdf
from backend.ingestion.chunk import split_text_into_chunks
from backend.database.repository_chunks import insert_chunk

def index_document(document_id: str, file_path: str) -> int:
    """Extraction and indexing of a PDF document into database."""

    # Extract text from the PDF
    pages = extract_text_from_pdf(file_path)

    # Split the extracted text into chunks
    chunks = split_text_into_chunks(document_id, pages)

    # Insert chunk into the database
    for chunk in chunks:
        insert_chunk(
            chunk_id=chunk['chnunk_id'],
            document_id=chunk['document_id'],
            chunk_index=chunk['chunk_index'],
            page_start=chunk['page_number'],
            page_end=chunk['page_number'],
            content=chunk['content'],
            metadata={}
        )

    return len(chunks)