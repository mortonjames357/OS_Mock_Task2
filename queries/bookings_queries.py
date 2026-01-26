import sqlite3

DB_PATH = './database/database.db'

def get_all_bookings():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("SELECT * FROM bookings")
            bookings = cursor.fetchall()

        return bookings
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def get_booking_by_id(booking_id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("SELECT * FROM bookings WHERE booking_id=?", (booking_id),)
            booking = cursor.fetchall()
        return booking
    except sqlite3.Error as e:
        print(f"Database error: {e}")


def create_booking(user_id, address, booking_date, booking_time, booking_type, booking_status, technican_id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("""
                            INSERT INTO bookings
                                (user_id, address, booking_date, booking_time, booking_type, booking_status, technican_id)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                            """, (user_id, address, booking_date, booking_time, booking_type, booking_status, technican_id,))
            
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def delete_booking(id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("DELETE FROM bookings WHERE booking_id=?", (id,))
            conn.commit()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        
