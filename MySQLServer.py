import mysql.connector
from mysql.connector import Error


def create_database():
    connection = None

    try:
        # Connect to MySQL server (no DB selected)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        # Create cursor to execute SQL
        cursor = connection.cursor()

        # Create database safely if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handle connection or execution errors
        print(f"Error: {e}")

    finally:
        # Ensure resources are properly closed
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == "__main__":
    create_database()