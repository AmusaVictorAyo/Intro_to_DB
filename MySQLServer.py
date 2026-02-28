import mysql.connector


def create_database():
    connection = None

    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        cursor = connection.cursor()

        # Create database safely
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Handle MySQL errors
        print(f"Error: {e}")

    finally:
        # Close DB connection properly
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == "__main__":
    create_database()