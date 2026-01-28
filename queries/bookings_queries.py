# Imports
import sqlite3

# Path to db
DB_PATH = './database/database.db'

# Function to get all data from bookings
def get_all_bookings():
    try:
        # Connect to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            # Execute the query
            cursor.execute("SELECT * FROM bookings")
            bookings = cursor.fetchall()
        # Return the data
        return bookings
    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# Function to get all data where id = input
def get_booking_by_id(booking_id):
    try:
        # Connect to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            # Execute the query
            cursor.execute("SELECT * FROM bookings WHERE booking_id=?", (booking_id),)
            booking = cursor.fetchall()
        # Return teh data
        return booking
    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# Function to create a booking
def create_booking(user_id, address, booking_date, booking_time, booking_type, booking_status, technican_id):
    try:
        # Connect to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            # Execute the query
            cursor.execute("""
                            INSERT INTO bookings
                                (user_id, address, booking_date, booking_time, booking_type, booking_status, technican_id)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                            """, (user_id, address, booking_date, booking_time, booking_type, booking_status, technican_id,))
            
            conn.commit()
    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# Function to delete a booking based on the inputted id
def delete_booking(id):
    try:
        # Connect to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            # Execute the query
            cursor.execute("DELETE FROM bookings WHERE booking_id=?", (id,))
            conn.commit()

    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        
