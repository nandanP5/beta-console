import sqlite3

conn = sqlite3.connect('databases/questions.db')
cursor = conn.cursor()

# Check table schema
cursor.execute("PRAGMA table_info(questions)")
columns = cursor.fetchall()

# Print the column names
for column in columns:
    print(column)

conn.close()

