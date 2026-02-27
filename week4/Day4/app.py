from flask import Flask, render_template, request
import sqlite3
import os
app = Flask(__name__)
DATABASE = 'my_database.db'
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
def insert_submission(name, email):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(
        'INSERT INTO submissions (name, email) VALUES (?, ?)',
        (name, email)
    )
    conn.commit()
    conn.close()
def get_all_submissions():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT id, name, email FROM submissions')
    rows = c.fetchall()
    conn.close()
    return rows
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name and email:
            insert_submission(name, email)
    entries = get_all_submissions()
    return render_template('form.html', entries=entries)
if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True)