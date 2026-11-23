# Student Management System

A command-line Student Management System developed using Python and PostgreSQL.

## Project Overview

This project manages student records through a Python application connected to a PostgreSQL database.

It is also a practical learning project focused on Python programming, relational database management, SQL queries, and database connectivity.

## Technologies Used

- Python 3
- PostgreSQL
- psycopg2
- python-dotenv
- Git and GitHub
- Visual Studio Code

## Current Features

1. Student registration
2. View all registered students
3. PostgreSQL database connectivity
4. Automatic student ID generation
5. Secure database credential management using environment variables

## Project Structure

Student_Management_System/
|-- database/
|   |-- db_connection.py
|-- models/
|   |-- student.py
|-- services/
|   |-- student_service.py
|-- utils/
|-- main.py
|-- requirements.txt
|-- .gitignore
|-- README.md

## Setup Instructions

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   pip install -r requirements.txt

4. Create a `.env` file in the project root and add:

   DB_PASSWORD=your_postgresql_password

5. Create the PostgreSQL database named `student_management_db`.
6. Run the application:

   python main.py

## Security

Database credentials are stored in a local `.env` file and excluded from version control through `.gitignore`.

Never upload your actual database password.

## Learning Objectives

- Python functions and modular programming
- PostgreSQL database connectivity
- SQL INSERT and SELECT operations
- Database transactions
- Environment variable management
- Git and GitHub version control

## Future Improvements

- Search for students
- Update student information
- Delete student records
- Department management
- Course management
- Student enrollment management
- Student reports

## Author

Ibrahim Adejimi

GitHub: https://github.com/iadejimi-Him
