import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'ingredients.db')

def show_all_ingredients():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute("SELECT name, info FROM ingredients")
    rows = cursor.fetchall()

    if not rows:
        print("📭 No ingredients stored yet.")
    else:
        for name, info in rows:
            print(f"\n🔹 Name: {name}\n---\n{info}\n{'='*40}")
    conn.close()

if __name__ == "__main__":
    show_all_ingredients()
