PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS "user" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT UNIQUE,
    password TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    roll_no TEXT UNIQUE,
    user_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES "user"(id) ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    assigned_to_student_id INTEGER,
    assigned_to_user_id INTEGER,
    due_date DATE,
    completed INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(assigned_to_student_id) REFERENCES students(id) ON DELETE SET NULL,
    FOREIGN KEY(assigned_to_user_id) REFERENCES "user"(id) ON DELETE SET NULL
);
INSERT OR IGNORE INTO "user" (id, username, email, password) 
VALUES
  (1, 'bhuvana', 'bhuvana3109@example.com', 'bhuvana123'),
  (2, 'dinamani', 'dinamani@example.com', 'dinamani123');
INSERT OR IGNORE INTO students (id, first_name, last_name, roll_no, user_id)
VALUES
  (1, 'bhuvana', 'K', 'S001', 1),
  (2, 'dinamani', 'M', 'o23', 2);
INSERT OR IGNORE INTO tasks (id, title, description, assigned_to_student_id, assigned_to_user_id, due_date, completed)
VALUES
  (1, 'Intro task', 'Task for Bhuvana', 1, 1, NULL, 0),
  (2, 'Intro task', 'Task for Dinamani', 2, 2, NULL, 0);