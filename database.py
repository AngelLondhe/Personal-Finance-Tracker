import sqlite3

conn = sqlite3.connect('finance.db')
cursor = conn.cursor()

# Creating table
cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    category TEXT,
                    amount REAL)''')

conn.commit()
conn.close()
