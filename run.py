from backend.app import app
from backend.db import init_db

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
