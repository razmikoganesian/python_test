import sqlite3

from numpy import short

DB_NAME = "database.db"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
                    CREATE TABLE IF NOT EXISTS urls(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    original_url TEXT NOT NULL,
                    short_code TEXT UNIQUE NOT NULL,
                    visit_count INTEGER DEFAULT 0
                    )
                    """)
        conn.commit()


def insert_url(original_url, short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            """
        INSERT INTO urls (original_url, short_code)
        VALUES (?,?)

        """,
            (original_url, short_code),
        )
        conn.commit()


def get_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("SELECT * FROM urls WHERE short_code = ?", (short_code,))
        return cursor.fetchone()


def increment_visit_count(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            """
            UPDATE urls
            SET visit_count = visit_count + 1
            WHERE short_code = ?
            """,
            (short_code,),
        )
        conn.commit()


def get_all_urls():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(
            "SELECT original_url, short_code, visit_count FROM urls ORDER by id DESC"
        )
        return cursor.fetchall()


def delete_url_by_code(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("DELETE FROM urls WHERE short_code = ?", (short_code,))
        conn.commit()
        return cursor.rowcount > 0
