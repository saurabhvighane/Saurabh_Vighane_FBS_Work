import hashlib
import mysql.connector
from database import create_connection

class User:

    def __init__(self):
        self.connection = create_connection()

        self.cursor = self.connection.cursor(dictionary=True)

    def hash_password(self, password):
        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    def register(self, username, password):
        hashed_password = self.hash_password(password)

        query = """
        INSERT INTO users (username, password)
        VALUES (%s, %s)
        """

        try:
            self.cursor.execute(
                query,
                (username, hashed_password)
            )

            self.connection.commit()
            return True

        except mysql.connector.IntegrityError:
            return False

    def login(self, username, password):
        hashed_password = self.hash_password(password)

        query = """
        SELECT * FROM users
        WHERE username = %s AND password = %s
        """

        self.cursor.execute(
            query,
            (username, hashed_password)
        )

        return self.cursor.fetchone()

    def save_history(
        self,
        user_id,
        searched_song,
        recommendations
    ):
        query = """
        INSERT INTO recommendation_history
        (
            user_id,
            searched_song,
            recommended_song,
            recommended_artist
        )
        VALUES (%s, %s, %s, %s)
        """

        for score, song in recommendations:

            self.cursor.execute(
                query,
                (
                    user_id,
                    searched_song,
                    song["title"],
                    song["artist"]
                )
            )

        self.connection.commit()

    def get_history(self, user_id):
        query = """
        SELECT *
        FROM recommendation_history
        WHERE user_id = %s
        ORDER BY recommendation_date DESC
        """

        self.cursor.execute(
            query,
            (user_id,)
        )

        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()