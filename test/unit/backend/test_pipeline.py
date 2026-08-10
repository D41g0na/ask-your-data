import uuid
from pathlib import Path
from unittest.mock import patch

from backend.ingestion.pipeline import index_document


@patch("backend.ingestion.pipeline.split_text_into_chunks")
@patch("backend.ingestion.pipeline.insert_chunks")
@patch("backend.ingestion.pipeline.extract_text_from_pdf")
def test_index_document(
    mock_extract,
    mock_insert_chunks,
    mock_split,
):
    document_id = str(uuid.uuid4())
    file_path = Path("/fake/path/document.pdf")

    mock_extract.return_value = [{"page": 1, "text": "Texte extrait"}]

    mock_insert_chunks.return_value = 1

    mock_split.return_value = [
        {
            "chunk_id": "chunk_1",
            "document_id": document_id,
            "chunk_index": 0,
            "page_start": 1,
            "page_end": 1,
            "content": "Premier chunk",
            "language": "fr",
        }
    ]

    result = index_document(document_id, file_path)

    assert result == 1

    mock_extract.assert_called_once_with(file_path)
    mock_split.assert_called_once_with(
        document_id,
        mock_extract.return_value,
    )

    mock_insert_chunks.assert_called_once_with(mock_split.return_value)