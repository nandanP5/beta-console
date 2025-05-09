import sqlite3

# Connect to the questions database
conn = sqlite3.connect('databases/questions.db')
c = conn.cursor()

# Drop table if exists (this ensures we're starting fresh each time)
c.execute("DROP TABLE IF EXISTS questions")

# Create table to store the questions
c.execute('''
    CREATE TABLE questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        db_name TEXT,
        difficulty TEXT,
        question_text TEXT,
        answer TEXT
    )
''')

# Sample data to insert into questions.db (you can add more questions later)
sample_questions = [
    ("hospital.db", "Easy", "List all patients", "SELECT * FROM patients;"),
    ("hospital.db", "Medium", "Find male patients", "SELECT * FROM patients WHERE gender = 'Male';"),
    ("company.db", "Easy", "List all employees", "SELECT * FROM employees;"),
    ("company.db", "Medium", "List employees in Engineering",
     "SELECT * FROM employees WHERE department_id = (SELECT id FROM departments WHERE name = 'Engineering');"),
    ("company.db", "Hard", "Count the number of employees in each department",
     "SELECT d.name, COUNT(e.id) FROM departments d LEFT JOIN employees e ON d.id = e.department_id GROUP BY d.name;"),
]

# Insert questions into the database
c.executemany('''
    INSERT INTO questions (db_name, difficulty, question_text, answer)
    VALUES (?, ?, ?, ?)
''', sample_questions)

# Commit the changes and close the connection
conn.commit()
conn.close()
print("✅ questions.db created and populated.")
