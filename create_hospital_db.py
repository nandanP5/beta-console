import sqlite3

conn = sqlite3.connect('databases/hospital.db')
c = conn.cursor()

# Drop table if it exists
c.execute("DROP TABLE IF EXISTS patients")

# Create table
c.execute('''
    CREATE TABLE patients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT
    )
''')

# Insert sample data
c.executemany('''
    INSERT INTO patients (id, name, age, gender)
    VALUES (?, ?, ?, ?)
''', [
    (1, 'Alice', 30, 'Female'),
    (2, 'Bob', 40, 'Male'),
    (3, 'Charlie', 25, 'Male'),
    (4, 'Diana', 35, 'Female')
])

conn.commit()
conn.close()
print("✅ hospital.db created.")
