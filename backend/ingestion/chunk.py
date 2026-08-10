import uuid

from langchain_text_splitters import RecursiveCharacterTextSplitter

import logging

logger = logging.getLogger(__name__)


def split_text_into_chunks(document_id, pages, chunk_size=500, chunk_overlap=100):
    """Split extracted PDF pages into overlapping text chunks."""

    # Split the documents into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    chunks = []
    chunk_index = 0

    for page in pages:
        page_number = page["page"]
        text = page["text"]
        page_language = page.get("language")

        if not text.strip():
            continue  # Skip empty pages

        split_texts = splitter.split_text(text)

        for chunk_text in split_texts:
            if not chunk_text.strip():
                continue  # Skip empty chunks

            chunks.append(
                {
                    "chunk_id": str(uuid.uuid4()),
                    "document_id": document_id,
                    "chunk_index": chunk_index,
                    "page_start": page_number,
                    "page_end": page_number,
                    "content": chunk_text,
                    "language": page_language,
                }
            )

            chunk_index += 1

        logger.info(
            "Split %s pages into %s chunks (size: %s, overlap=%s)",
            len(pages),
            len(chunks),
            chunk_size,
            chunk_overlap,
        )

    return chunks
