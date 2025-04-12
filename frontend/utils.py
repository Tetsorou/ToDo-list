import sqlite3
import os

def get_db_connection() -> sqlite3.Connection:
    """Create a connection to the SQLite database."""
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def get_tasks() -> list:
    """Fetch all tasks from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    return tasks



