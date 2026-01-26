import os
import sqlite3

DB_PATH = './database/app_database.db'
SEED_PATH = './database/seed.sql'

def steup_db():
     with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )""")
        
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
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS technicians (
                technican_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
            )""")
        
        conn.commit()


def seed_DB()
        
