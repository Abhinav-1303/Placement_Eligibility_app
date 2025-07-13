import sqlite3  # This is Python’s built-in module to work with SQLite databases

# Create or open a database file named 'Students.db'
conn = sqlite3.connect('Students.db')  

# Create a cursor object to execute SQL commands
cur = conn.cursor()  

# SQL command to create a table called 'Students' if it doesn't already exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID that auto-increments for each new entry
        Name TEXT NOT NULL,                    -- Student's name (required)
        Roll_Number TEXT NOT NULL,             -- Student's roll number (required)
        Department TEXT NOT NULL,              -- Department name (required)
        CGPA REAL NOT NULL,                    -- CGPA as a decimal value (e.g., 7.5)
        Eligibility TEXT NOT NULL,             -- "Eligible for placement" or "Not Eligible for placement"
        Grade TEXT NOT NULL                    -- Grade like A+, B, etc.
    )
''')

# Save the changes in the database
conn.commit()

# Close the database connection
conn.close()
