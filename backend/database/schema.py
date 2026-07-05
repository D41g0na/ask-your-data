from .connection import get_connection


def create_documents_table():
    """Create the documents table in the database if it doesn't exist."""

    query = """
        CREATE TABLE IF NOT EXISTS documents (
            document_id UUID PRIMARY KEY,
            filename TEXT NOT NULL,
            file_path TEXT NOT NULL,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            metadata JSONB
        );
    """

    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()
    finally:
        conn.close()


def create_chunks_table():
    """Create the chunk table in the database if it doesn't exist."""

    query = """
        CREATE TABLE IF NOT EXISTS chunks (
            chunk_id UUID PRIMARY KEY,
            document_id UUID NOT NULL REFERENCES documents(document_id) ON DELETE CASCADE,
            chunk_index INTEGER NOT NULL,
            page_start INTEGER NOT NULL,
            page_end INTEGER NOT NULL,
            content TEXT NOT NULL,
            metadata JSONB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """

    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    create_documents_table()
    create_chunks_table()
