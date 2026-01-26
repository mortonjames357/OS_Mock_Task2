#Imports
import os
import sqlite3

# Constants
DB_PATH = './database/database.db'
SEED_PATH = './database/seed.sql'

# Function to set up the database
def setup_DB():
     # Creating connecting to the database
     with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        # Creating user table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )""")
        
        # Creating technicians table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS technicians (
                technican_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL
            )""")
        
        # Creating bookings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                address TEXT,
                booking_date TEXT NOT NULL,
                booking_time TEXT NOT NULL,
                booking_type TEXT NOT NULL,
                booking_status TEXT NOT NULL,
                technican_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (technican_id) REFERENCES technicians(technican_id)
            )""")
        
        
        
        
        conn.commit()

# Function to seed the database
def seed_DB():
    # Connecting to the db
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("SELECT COUNT(*) FROM bookings")
            if cursor.fetchone()[0] > 0:
                print("Database already seeded.")
                return

            with open(SEED_PATH, 'r', encoding='utf-8') as f:
                seed_sql = f.read()
                # executescript automatically issues a COMMIT before executing
                cursor.executescript(seed_sql)
            
            print("Database seeded successfully.")
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

        
