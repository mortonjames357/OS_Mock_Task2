# Imports
import sqlite3

# Path to the database
DB_PATH = './database/database.db'

# Function to get all data from appointments table
def get_all_appointments():
    try:
        # Connecting to database
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            # Executing the query
            cursor.execute("SELECT * FROM salesmenAppointments")
            appoints = cursor.fetchall()

        # Returning the data
        return appoints
    
    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")


# Function to get appointment by inputted ID
def get_appoint_by_id(id):
    try:
        # Connect to the database
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            # Execute the query
            cursor.execute("SELECT * FROM salesmenAppointments WHERE appointment_id=?", (id,))
            appoint = cursor.fetchall()

        # Return the data
        return appoint
    
    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")


# Function to create an appointment
def create_appoint(name, email, reason):
    try:
        # Connecting to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            # Executing the query
            cursor.execute("""
                            INSERT INTO salesmenAppointments
                                (name, email, appoint_reason)
                            VALUES (?,?,?)
                            """, (name, email, reason,))
            conn.commit()
    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")


# Function to delete an apppointment
def delete_appoint(id):
    try:
        # Connecting to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            # Executing the query
            cursor.execute("DELETE FROM salesmenAppointments WHERE appointment_id=?", (id,))
            conn.commit()
            
    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")
