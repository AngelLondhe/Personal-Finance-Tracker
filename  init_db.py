import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create 'expenses' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT
)
''')

# Save (commit) changes and close the connection
conn.commit()
conn.close()

print("✅ Database and 'expenses' table created successfully!")
