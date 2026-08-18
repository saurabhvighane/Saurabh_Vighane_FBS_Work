import mysql.connector
from mysql.connector import Error


def get_connection():

    try:

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="bank_management"
        )

        return connection

    except Error as e:

        print(f"Database connection error: {e}")
        return None