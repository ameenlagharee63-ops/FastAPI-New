import sqlite3

# 1. Database connection banayein
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

print("Database connected successfully")

# 2. Table create karein
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

# 3. Data insert karein (Sahi syntax)
cursor.execute("INSERT INTO users (name) VALUES (?)", ("AMEEN",))

# 4. Changes ko save (commit) karein
connection.commit()

# 5. Data ko check karne ke liye fetch karein
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Database ka Data:")
for row in rows:
    print(row)

# 6. Connection close kar dein
connection.close()