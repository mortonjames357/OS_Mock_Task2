import sqlite3

DB_PATH = './database/database.db'

def get_all_techs():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            
            cursor.execute("SELECT * FROM technicians")
            techs = cursor.fetchall()
            
        return techs
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return
    
def get_tech_by_id(tech_id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("SELECT * FROM technicians WHERE technician_id=?", (tech_id,))
            tech = cursor.fetchall()

        return tech
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return
    
def create_tech(name, department):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("INSERT INTO technicians (name, department) VALUES (?, ?)", (name, department,))
            conn.commit()

    except sqlite3.Error as e:
        print(f"Database error: {e}")

def delete_tech(tech_id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("DELETE FROM technicians WHERE technician_id=?", (tech_id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")