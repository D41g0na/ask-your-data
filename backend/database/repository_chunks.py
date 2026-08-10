from psycopg.types.json import Json

from .connection import get_connection


def insert_chunks(chunks: list[dict]) -> int:
    """Insert a batch of chunks into the database in a single transaction."""

    if not chunks:
        return 0

    query = """
        INSERT INTO chunks (
            chunk_id,
            document_id,
            chunk_index,
            page_start,
            page_end,
            content,
            metadata,
            language
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """

    values = [
        (
            c["chunk_id"],
            c["document_id"],
            c["chunk_index"],
            c["page_start"],
            c["page_end"],
            c["content"],
            Json(c.get("metadata", {})),
            c["language"],
        )
        for c in chunks
    ]

    with get_connection() as conn, conn.cursor() as cur:
        cur.executemany(query, values)
        return cur.rowcount
