from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course TEXT,
        phone TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route("/")
def index():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()
    return render_template("list.html", students=data)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        phone = request.form["phone"]

        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO students (name, course, phone) VALUES (?, ?, ?)",
                    (name, course, phone))
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        phone = request.form["phone"]

        cur.execute("UPDATE students SET name=?, course=?, phone=? WHERE id=?",
                    (name, course, phone, id))
        conn.commit()
        conn.close()
        return redirect("/")

    cur.execute("SELECT * FROM students WHERE id=?", (id,))
    student = cur.fetchone()
    conn.close()
    return render_template("edit.html", student=student)


@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)