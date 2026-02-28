from flask import Flask, render_template, request, redirect, session
import sqlite3
app = Flask(__name__)
app.secret_key = "secret123"
def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn
def create_table():
    conn = get_db()
    conn.execute
    user = conn.execute("SELECT * FROM users WHERE username='Bhuvana'").fetchone()
    if not user:
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("Bhuvana", "Bhuvi@09"))
    conn.commit()
    conn.close()
@app.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()
        if user:
            session["user"] = username
            return redirect("/dashboard")
        else:
            error = "Invalid Username or Password"
    return render_template("login.html", error=error)
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect("/")
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")
if __name__ == "__main__":
    create_table()
    app.run(debug=True)