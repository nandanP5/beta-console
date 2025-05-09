from flask import Flask, render_template, request, jsonify
import sqlite3
import json
import os

app = Flask(__name__)

# Load database paths
DATABASES = ["hospital.db", "company.db", "questions.db"]

@app.route('/')
def index():
    # Connect to the 'questions.db' to get the questions from the database
    conn = sqlite3.connect('databases/questions.db')
    cursor = conn.cursor()
    
    # Fetch all questions from the 'questions' table
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()  # This will fetch all rows from the table
    
    # Close the database connection
    conn.close()

    # Return the rendered template with the questions
    return render_template('index.html', questions=questions, databases=DATABASES)

@app.route('/run_query', methods=['POST'])
def run_query():
    data = request.json
    db_name = data['db']
    user_query = data['query']
    question_id = data['question_id']

    # Fetch the correct answer from the database
    conn = sqlite3.connect(f'databases/{db_name}')
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM questions WHERE id = ?", (question_id,))
    correct_query = cursor.fetchone()[0]

    try:
        # Run user query
        cursor.execute(user_query)
        user_result = cursor.fetchall()
        user_columns = [desc[0] for desc in cursor.description]

        # Run correct query
        cursor.execute(correct_query)
        correct_result = cursor.fetchall()
        correct_columns = [desc[0] for desc in cursor.description]

        conn.close()

        is_correct = (user_result == correct_result) and (user_columns == correct_columns)

        return jsonify({
            'columns': user_columns,
            'rows': user_result,
            'is_correct': is_correct,
            'correct_result': correct_result
        })

    except Exception as e:
        return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True)
