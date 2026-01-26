import sqlite3

DB_PATH = './database/database.db'

def get_all_users():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        
        cursor.execute("SELECT user_id, username, email FROM users")
        users = cursor.fetchall()
        
    return users

def get_user_by_id(user_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        
        cursor.execute("SELECT user_id, username, email FROM users WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()
        
    return user

def create_user(username, email, password):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password,))
            conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error creating user: {e}")

def delete_user(user_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("DELETE FROM users WHERE user_id=?", (user_id,))
        conn.commit()

