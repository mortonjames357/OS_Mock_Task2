import sqlite3

DB_PATH = './database/database.db'

def get_all_users():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            
            cursor.execute("SELECT user_id, username, email FROM users")
            users = cursor.fetchall()
            
        return users
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return

def get_user_by_id(user_id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            
            cursor.execute("SELECT user_id, username, email FROM users WHERE user_id = ?", (user_id,))
            user = cursor.fetchone()
            
        return user
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return

def create_user(username, email, password):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            cursor.execute("PRAGMA foreign_keys = ON;")
            
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating user: {e}")

def delete_user(user_id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("DELETE FROM users WHERE user_id=?", (user_id,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting user: {e}")


