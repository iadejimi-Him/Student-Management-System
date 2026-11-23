
import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from the project root
load_dotenv()


def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="student_management_db",
            user="postgres",
            password=os.getenv("DB_PASSWORD"),
            port="5432"
        )

        print("Database connection successful!")
        return connection

    except psycopg2.Error as error:
        print("Database connection failed:", error)
        return None
