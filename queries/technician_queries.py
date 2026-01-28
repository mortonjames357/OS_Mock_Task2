# Imports
import sqlite3

# Path to the db
DB_PATH = './database/database.db'

# Function to get all data about technicians
def get_all_techs():
    try:
        # Connect to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            
            # Execute the query
            cursor.execute("SELECT * FROM technicians")
            techs = cursor.fetchall()        
        # Return the data
        return techs
    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return

# Function to get all techs where the id matches
def get_tech_by_id(tech_id):
    try:
        # Connect to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            
            # Execute the query
            cursor.execute("SELECT * FROM technicians WHERE technican_id = ?", (tech_id,))
            tech = cursor.fetchall()
        # Return the data
        return tech
    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return

# Function to create a technicaian
def create_tech(name, department):
    try:
        # Connect to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            # Execute the query
            cursor.execute("INSERT INTO technicians (name, department) VALUES (?, ?)", (name, department,))
            conn.commit()

    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# Function to delete tech where id = input
def delete_tech(tech_id):
    try:
        # Connect to the db
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            # Execute yje query
            cursor.execute("DELETE FROM technicians WHERE technician_id=?", (tech_id))
            conn.commit()
    # Error handling
    except sqlite3.Error as e:
        print(f"Database error: {e}")