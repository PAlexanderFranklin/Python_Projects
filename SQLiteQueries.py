import apsw

db = apsw.Connection("./SQLiteDB/chinook.db")
cursor1 = db.cursor()
cursor1.execute("""
SELECT *
FROM employees
""")
print(cursor1.fetchall())
