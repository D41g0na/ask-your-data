from psycopg.types.json import Json

from .connection import get_connection


def insert_document(document_id, filename, file_path, metadata):
    """Insert a new document into the database."""

    query = """
        INSERT INTO documents (document_id, filename, file_path, metadata)
        VALUES (%s, %s, %s, %s)
        RETURNING document_id;
    """

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, (document_id, filename, file_path, Json(metadata)))
            result = cur.fetchone()

        conn.commit()

        return str(result[0])

    finally:
        conn.close()
