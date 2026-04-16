import sqlite3

DB_NAME = "chat.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room TEXT NOT NULL,
            username TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_message(room: str, username: str, message: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages (room, username, message) VALUES (?, ?, ?)",
        (room, username, message)
    )
    conn.commit()
    conn.close()

def get_messages(room: str, limit: int = 50):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, message, timestamp FROM messages WHERE room = ? ORDER BY timestamp ASC LIMIT ?",
        (room, limit)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows