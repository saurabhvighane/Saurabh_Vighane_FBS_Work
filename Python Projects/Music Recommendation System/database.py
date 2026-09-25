import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="saurabh10.",
        database="music_recommendation"
    )

    return connection