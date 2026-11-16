import sqlite3

DB_PATH = "readiness.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Parts inventory table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            part_id TEXT PRIMARY KEY,
            part_name TEXT NOT NULL,
            quantity_in_stock INTEGER NOT NULL,
            warehouse_location TEXT
        )
    """)
    
    # Maintenance work orders table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS work_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipment_id TEXT NOT NULL,
            fault_code TEXT,
            issue_description TEXT NOT NULL,
            status TEXT DEFAULT 'OPEN'
        )
    """)
    
    conn.commit()
    conn.close()
