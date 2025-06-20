import sqlite3

# Connect to the databse (or create it)
def connect():
    return sqlite3.connect("habit_tracker.db")

def create_table(conn):
    # Create a cursor to interact with the DB
    cur = conn.cursor()

    # Create users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
    """)

    # Create habits table (Foreign key will be here)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS habits(
            habit_id INTEGER PRIMARY KEY,
            habit_name TEXT,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(user_id))
    """)

    # Save changes
    conn.commit()
