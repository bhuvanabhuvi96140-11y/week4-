from pathlib import Path
import sqlite3
import sys
def main(sqlfile: str = 'database.sql'):
    sql_path = Path(__file__).with_name(sqlfile)
    if not sql_path.exists():
        print(f'Error: {sql_path} not found')
        return 1
    sql = sql_path.read_text(encoding='utf-8')
    db_path = Path(__file__).resolve().parents[1] / 'db.sqlite3'
    conn = sqlite3.connect(str(db_path))
    try:
        cur = conn.cursor()
        cur.executescript(sql)
        conn.commit()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tables = [r[0] for r in cur.fetchall()]
        print('Tables:', tables)
        queries = ("SELECT * FROM \"user\";", "SELECT * FROM students;", "SELECT * FROM tasks;")
        for q in queries:
            try:
                cur.execute(q)
                rows = cur.fetchall()
                print('\n' + q)
                if not rows:
                    print('  (no rows)')
                for r in rows:
                    print(' ', r)
            except Exception as e:
                print('Query error for', q, e)
    finally:
        conn.close()
    return 0
if __name__ == '__main__':
    sys.exit(main())
