from pathlib import Path
import sqlite3
import sys
def main():
    db_path = Path(__file__).resolve().parents[1] / 'db.sqlite3'
    conn = sqlite3.connect(str(db_path))
    try:
        cur = conn.cursor()
        cur.execute("UPDATE tasks SET title = ?, description = ? WHERE id = ?",
                    ("Task for Bhuvana", "Task assigned to Bhuvana", 1))
        cur.execute("UPDATE tasks SET title = ?, description = ? WHERE id = ?",
                    ("Task for Keerthana", "Task assigned to Keerthana", 2))
        conn.commit()
        cur.execute("SELECT * FROM tasks ORDER BY id")
        rows = cur.fetchall()
        print('Tasks after update:')
        for r in rows:
            print(' ', r)
    finally:
        conn.close()
if __name__ == '__main__':
    sys.exit(main())
