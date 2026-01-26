#Imports
import os
import sqlite3

# Constants
DB_PATH = './database/app_database.db'
SEED_PATH = './database/seed.sql'

# Function to set up the database
def setup_db():
     # Creating connecting to the database
     with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        # Creating user table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )""")
        
        # Creating bookings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                booking_date DATE NOT NULL,
                booking_time TIME NOT NULL,
                booking_type TEXT NOT NULL,
                booking_status TEXT NOT NULL,
                technican_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )""")
        
        # Creating technicians table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS technicians (
                technican_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
            )""")
        
        conn.commit()

# Function to seed the database
def seed_DB():
    # Connecting to the db
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        # Check if the users table already has data
        cursor.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] > 0:
            print("Database already seeded. Skipping seeding process.")
            return

        # Read and execute the seed SQL file
        with open(SEED_PATH, 'r') as f:
            seed_sql = f.read()
            
        cursor.executescript(seed_sql)
        conn.commit()
        
