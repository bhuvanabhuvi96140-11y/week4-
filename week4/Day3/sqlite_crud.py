import os
import sqlite3
DB_NAME = 'sqlite_crud.db'
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')
conn.commit()
def create_user(name, age):
    """Insert a new user and return the new row id."""
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    return cursor.lastrowid
def get_users():
    """Return all users as a list of tuples (id, name, age)."""
    cursor.execute("SELECT id, name, age FROM users")
    return cursor.fetchall()
def get_user(user_id):
    """Return a single user by ID or None if not found."""
    cursor.execute("SELECT id, name, age FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()
def update_user(user_id, name=None, age=None):
    """Update name and/or age for the given user id."""
    if name is not None and age is not None:
        cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
    elif name is not None:
        cursor.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
    elif age is not None:
        cursor.execute("UPDATE users SET age = ? WHERE id = ?", (age, user_id))
    conn.commit()
def delete_user(user_id):
    """Delete the user with the specified id."""
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
if __name__ == "__main__":
    print("Inserting users...")
    id1 = create_user("bhuvana", 22)
    id2 = create_user("dinamani", 23)
    print("Current users:", get_users())
    try:
        sel = int(input("Enter a user ID to select: "))
        print("Selected user:", get_user(sel))
    except ValueError:
        print("Invalid ID entered, skipping single select.")
    print("Updating user", id1, "...")
    update_user(id1, age=22)
    print("Users after update:", get_users())
    print("Deleting user", id2, "...")
    delete_user(id2)
    print("Users after delete:", get_users())
    conn.close()