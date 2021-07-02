import apsw

db = apsw.Connection("./SQLiteDB/chinook.db")
cursor1 = db.cursor()
cursor1.execute("""
SELECT *
FROM employees
LIMIT 10;
""")
print(cursor1.fetchall(), '\n')

cursor2 = db.cursor()
cursor2.execute("""
SELECT Composer, SUM(Milliseconds)
FROM tracks
WHERE MediaTypeId != 3
GROUP BY Composer
ORDER BY SUM(Milliseconds) DESC
LIMIT 10;
""")
print(cursor2.fetchall(), '\n')

cursor3 = db.cursor()
cursor3.execute("""
SELECT Name, MediaTypeId, Milliseconds
FROM tracks
WHERE MediaTypeId != 3
ORDER BY Milliseconds DESC
LIMIT 10
""")
print(cursor3.fetchall(), '\n')