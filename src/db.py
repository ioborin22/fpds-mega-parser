import psycopg2
from psycopg2.extras import DictCursor

DB_CONFIG = {
    "dbname": "govinsight",
    "user": "iliaoborin",
    "password": "V%614ed5",
    "host": "127.0.0.1",
    "port": "5432",
}

def get_db_connection():
    """Creates and returns a database connection"""
    try:
        conn = psycopg2.connect(**DB_CONFIG, cursor_factory=DictCursor)
        return conn
    except Exception as e:
        print(f"⚠️ Database connection error: {e}")
        return None