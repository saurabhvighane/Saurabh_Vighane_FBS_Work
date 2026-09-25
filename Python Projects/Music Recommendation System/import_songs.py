import csv
import mysql.connector
from database import create_connection

# Connect to MySQL
connection = create_connection()
cursor = connection.cursor()

# Open CSV file
with open("songs_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    query = """
    INSERT INTO songs
    (song_id, title, artist, genre, language, mood)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    for row in reader:
        values = (
            row["song_id"],
            row["title"],
            row["artist"],
            row["genre"],
            row["language"],
            row["mood"]
        )

        cursor.execute(query, values)

connection.commit()

print("Songs imported successfully!")

cursor.close()
connection.close()