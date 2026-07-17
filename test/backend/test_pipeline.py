import uuid
from pathlib import Path
from unittest.mock import patch

from backend.ingestion.pipeline import index_document


@patch("backend.ingestion.pipeline.split_text_into_chunks")
@patch("backend.ingestion.pipeline.insert_chunk")
@patch("backend.ingestion.pipeline.extract_text_from_pdf")
def test_index_document(
    mock_extract,
    mock_insert_chunk,
    mock_split,
    
):
    document_id = str(uuid.uuid4())
    file_path = Path(__file__).parent / "test_extract.pdf"

    mock_extract.return_value = [{"page_number": 1, "content": "Texte extrait"}]

    mock_split.return_value = [
        {
            "chunk_id": "chunk_1",
            "document_id": document_id,
            "chunk_index": 0,
            "page_start": 1,
            "page_end": 1,
            "content": "Premier chunk",
            "metadata": {},
        }
    ]

    result = index_document(document_id, file_path)

    assert result == 1

    mock_extract.assert_called_once_with(file_path)
    mock_split.assert_called_once_with(
        document_id,
        mock_extract.return_value,
    )

    mock_insert_chunk.assert_called_once_with(
        chunk_id="chunk_1",
        document_id=document_id,
        chunk_index=0,
        page_start=1,
        page_end=1,
        content="Premier chunk",
        metadata={},
    )
