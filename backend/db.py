import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'ingredients.db')

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS ingredients (
                name TEXT PRIMARY KEY,
                info TEXT
            )
        ''')
        conn.commit()

def get_info(name):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute('SELECT info FROM ingredients WHERE name = ?', (name,))
        row = cursor.fetchone()
        return row[0] if row else None

def save_info(name, info):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('INSERT OR REPLACE INTO ingredients (name, info) VALUES (?, ?)', (name, info))
        conn.commit()
