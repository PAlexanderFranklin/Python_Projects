import sqlite3

chinookDB = sqlite3.connect("./SQLiteDB/chinook.db")
cursor1 = chinookDB.cursor()
cursor1.execute("""
SELECT *
FROM employees;
""")
print(cursor1.fetchall(), '\n')

cursor2 = chinookDB.cursor()
cursor2.execute("""
SELECT Composer, SUM(Milliseconds) AS length
FROM tracks
WHERE MediaTypeId != 3
GROUP BY Composer
ORDER BY length DESC
LIMIT 10;
""")
print("Composers with the longest total tracks: ", cursor2.fetchall(), '\n')

cursor3 = chinookDB.cursor()
cursor3.execute("""
SELECT Name, Milliseconds
FROM tracks
WHERE MediaTypeId != 3
ORDER BY Milliseconds DESC
LIMIT 10;
""")
print("Longest non-audio book tracks: ", cursor3.fetchall(), '\n')

genre = input("Enter a genre: ")
#genre = "Rock"

cursor4 = chinookDB.cursor()
cursor4.execute("""
SELECT Name, Composer
FROM tracks
WHERE GenreId = (
    SELECT GenreId
    FROM genres
    WHERE Name = (?)
);
""", (genre, ))
genreTracks = cursor4.fetchall()
print("Tracks in the " + genre + " genre:", genreTracks, '\n')

if (len(genreTracks) > 100):
    print(genre + " is a popular genre. \n")
else:
    print(genre + " is not very popular. \n")


cursor5 = chinookDB.cursor()
cursor5.execute("""
SELECT genres.Name, genres.GenreId, COUNT(TrackId) AS quantity
FROM genres
    JOIN tracks ON genres.GenreId = tracks.GenreID
GROUP BY genres.Name
ORDER BY quantity DESC;
""")
print("Tracks in each Genre: ", cursor5.fetchall(), '\n')