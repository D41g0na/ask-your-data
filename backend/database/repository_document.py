from psycopg.types.json import Json

from .connection import get_connection


def insert_document(document_id: str, filename: str, file_path: str, metadata: dict) -> int:
    """Insert a new document into the database."""

    query = """
        INSERT INTO documents (document_id, filename, file_path, metadata)
        VALUES (%s, %s, %s, %s);
    """

    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(query, (document_id, filename, file_path, Json(metadata)))
        return cur.rowcount
