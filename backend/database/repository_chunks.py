from psycopg.types.json import Json

from .connection import get_connection


def insert_chunk(
    chunk_id, document_id, chunk_index, page_start, page_end, content, metadata
):
    """Insert a new chunk into the database."""

    query = """
        INSERT INTO chunks (
            chunk_id,
            document_id,
            chunk_index,
            page_start,
            page_end,
            content,
            metadata
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING chunk_id;
    """

    values = (
        chunk_id,
        document_id,
        chunk_index,
        page_start,
        page_end,
        content,
        Json(metadata),
    )

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, values)
            result = cur.fetchone()

        conn.commit()

        return str(result[0])

    finally:
        conn.close()
