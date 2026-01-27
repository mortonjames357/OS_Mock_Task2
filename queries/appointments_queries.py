import sqlite3

DB_PATH = './database/database.db'

def get_all_appointments():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("SELECT * FROM salesmenAppointments")
            appoints = cursor.fetchall()

        return appoints
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
