import uuid

import pytest

from backend.database.repository_document import insert_document


@pytest.fixture
def document_id():
    document_id = str(uuid.uuid4())

    insert_document(
        document_id,
        filename="test_document.pdf",
        file_path="/path/to/test_doc.txt",
        metadata={"author": "John Doe"},
    )

    return document_id
