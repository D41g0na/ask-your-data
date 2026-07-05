from backend.database.connection import get_connection


def test_get_connection():
    # Test that a connection can be established
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("SELECT current_user;")
        result = cur.fetchone()
    conn.close()

    assert result[0] == "user"
    assert result is not None
    assert len(result) == 1
