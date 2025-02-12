from db import get_db_connection

def test_db():
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print(f"✅ Connected to DB: {db_version[0]}")
        conn.close()
    else:
        print("❌ Connection failed.")

test_db()