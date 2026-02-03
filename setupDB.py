#Imports
import os
import sqlite3
from werkzeug.security import generate_password_hash
from queries.users_queries import create_user

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
        
        # Creating appointments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS salesmenAppointments (
                appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                appoint_reason TEXT NOT NULL
            )""")
        
        
        
        
        conn.commit()

# Function to seed the database
def seed_DB():
    # Connecting to the db
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            # Checking if there is any data in bookings
            cursor.execute("SELECT COUNT(*) FROM bookings")
            if cursor.fetchone()[0] > 0:
                print("Database already seeded.")
                return
            
            # Seed users
            users = [
                ("admin", "admin@example.com", "admin123"),
                ("user1", "user1@example.com", "password1"),
                ("user2", "user2@example.com", "password2"),
                ("user3", "user3@example.com", "password3"),
                ("user4", "user4@example.com", "password4"),
            ]

            for username, email, password in users:
                hashed_pw = generate_password_hash(password)
                create_user(username, email, hashed_pw)

            # Seeding the database
            with open(SEED_PATH, 'r', encoding='utf-8') as f:
                seed_sql = f.read()
                cursor.executescript(seed_sql)
            
            print("Database seeded successfully.")
            conn.commit()
    # Error handling
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Function to call the other two functions  
def start_database():
    setup_DB()
    seed_DB()
