# Imports
import sqlite3

# Path to the db
DB_PATH = './database/database.db'

# Function to get all data about users
def get_all_users():
    try:
        # Connect to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            
            # Execute the query
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
        
        # Return the data
        return users
    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return

# Function to get data about user where id = input
def get_user_by_id(user_id):
    try:
        # Connect to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            
            # Execute thje query
            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            user = cursor.fetchall()
        # Return the data
        return user
    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return

# Function to create a user
def create_user(username, email, password):
    try:
        # Connect to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            
            # Execute the query
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password,))
            conn.commit()
    # Error handling
    except sqlite3.Error as e:
        print(f"Error creating user: {e}")

# Function to delete a user
def delete_user(user_id):
    try:
        # Connect to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            # Execute the query
            cursor.execute("DELETE FROM users WHERE user_id=?", (user_id,))
            conn.commit()
    # Error handling
    except sqlite3.Error as e:
        print(f"Error deleting user: {e}")

# Function to get user by email
def get_user_by_email():
    pass