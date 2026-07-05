import uuid

from backend.ingestion.chunk import split_text_into_chunks


def test_split_text_into_chunks():
    document_id = str(uuid.uuid4())
    pages = [
        {"page": 1, "text": "Le machine learning utilise des données pour apprendre."},
        {"page": 2, "text": "L'apprentissage automatique se base sur des datasets."},
        {"page": 3, "text": "Paris est la capitale de la France."},
    ]

    chunks = split_text_into_chunks(
        document_id=document_id, pages=pages, chunk_size=500, chunk_overlap=100
    )

    assert isinstance(chunks, list)
    assert len(chunks) == 3

    first_chunk = chunks[0]

    assert first_chunk["document_id"] == document_id
    assert first_chunk["chunk_index"] == 0
    assert first_chunk["page_start"] == 1
    assert first_chunk["page_end"] == 1
    assert "machine learning" in first_chunk["content"]

    assert "chunk_id" in first_chunk
