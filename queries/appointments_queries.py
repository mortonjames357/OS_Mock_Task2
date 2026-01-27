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



def get_appoint_by_id(id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("SELECT * FROM salesmenAppointments WHERE appointment_id=?", (id,))
            appoint = cursor.fetchall()

        return cursor
    except sqlite3.Error as e:
        print(f"Database error: {e}")



def create_appoint(name, email, reason):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("""
                            INSERT INTO salesmenAppointments
                                (name, email, appoint_reason)
                            VALUES (?,?,?)
                            """, (name, email, reason,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")



def delete_appoint(id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("DELETE FROM salesmenAppointments WHERE appointment_id=?", (id,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
