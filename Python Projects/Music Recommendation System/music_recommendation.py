import mysql.connector
from database import create_connection

class MusicRecommendationSystem:

    def __init__(self):
        self.connection = create_connection()
        self.cursor = self.connection.cursor(dictionary=True)

    def search_song(self, title):
        query = """
        SELECT * FROM songs
        WHERE LOWER(title) LIKE LOWER(%s)
        """

        search = "%" + title + "%"

        self.cursor.execute(query, (search,))
        return self.cursor.fetchall()

    def calculate_score(self, song, reference):
        score = 0

        if song["genre"].lower() == reference["genre"].lower():
            score += 3

        if song["language"].lower() == reference["language"].lower():
            score += 2

        if song["mood"].lower() == reference["mood"].lower():
            score += 3

        return score

    def get_recommendations(self, selected_song):
        query = """
        SELECT * FROM songs
        WHERE song_id != %s
        """

        self.cursor.execute(
            query,
            (selected_song["song_id"],)
        )

        songs = self.cursor.fetchall()

        recommendations = []

        for song in songs:
            score = self.calculate_score(
                song,
                selected_song
            )

            recommendations.append((score, song))

        recommendations.sort(
            key=lambda x: x[0],
            reverse=True
        )

        return recommendations[:5]

    def get_preferences_options(self):
        self.cursor.execute(
            "SELECT DISTINCT genre FROM songs"
        )
        genres = [
            row["genre"]
            for row in self.cursor.fetchall()
        ]

        self.cursor.execute(
            "SELECT DISTINCT language FROM songs"
        )
        languages = [
            row["language"]
            for row in self.cursor.fetchall()
        ]

        self.cursor.execute(
            "SELECT DISTINCT mood FROM songs"
        )
        moods = [
            row["mood"]
            for row in self.cursor.fetchall()
        ]

        return genres, languages, moods

    def get_recommendations_by_preferences(
        self,
        genre,
        language,
        mood
    ):
        query = """
        SELECT * FROM songs
        """

        self.cursor.execute(query)
        songs = self.cursor.fetchall()

        reference = {
            "genre": genre,
            "language": language,
            "mood": mood
        }

        recommendations = []

        for song in songs:
            score = self.calculate_score(
                song,
                reference
            )

            recommendations.append((score, song))

        recommendations.sort(
            key=lambda x: x[0],
            reverse=True
        )

        return recommendations[:5]

    def close_connection(self):
        self.cursor.close()
        self.connection.close()