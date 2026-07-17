import os

from backend.database.connection import get_connection


def test_get_connection():
    # Test that a connection can be established
    expected_user = os.environ["POSTGRES_USER"]

    conn = get_connection()

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT current_user;")
            result = cur.fetchone()
    finally:
        conn.close()

    assert result is not None
    assert len(result) == 1
    assert result[0] == expected_user
