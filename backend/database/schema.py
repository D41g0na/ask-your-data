from .connection import get_connection


def create_documents_table() -> None:
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

    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(query)


def create_chunks_table() -> None:
    """Create the chunk table in the database if it doesn't exist."""

    query = """
        CREATE TABLE IF NOT EXISTS chunks (
            chunk_id UUID PRIMARY KEY,
            document_id UUID NOT NULL REFERENCES documents(document_id) ON DELETE CASCADE,
            chunk_index INTEGER NOT NULL,
            language TEXT NOT NULL,
            page_start INTEGER NOT NULL,
            page_end INTEGER NOT NULL,
            content TEXT NOT NULL,
            metadata JSONB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """

    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(query)

def alter_chunks_table_add_language() -> None:
    """Alter the chunks table to add a language column if it doesn't exist."""

    query = """
        ALTER TABLE chunks
        ADD COLUMN IF NOT EXISTS language TEXT NOT NULL DEFAULT 'unknown';
    """

    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(query)


if __name__ == "__main__":
    #create_documents_table()
    #create_chunks_table()
    alter_chunks_table_add_language()
