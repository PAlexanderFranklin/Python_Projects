import apsw

db = apsw.Connection("./SQLiteDB/chinook.db")
cursor1 = db.cursor()
cursor1.execute("""
SELECT *
FROM employees;
""")
#print(cursor1.fetchall())

cursor2 = db.cursor()
cursor2.execute("""
SELECT Composer, SUM(Milliseconds)
FROM tracks
GROUP BY Composer
LIMIT 10;
""")
print(cursor2.fetchall())