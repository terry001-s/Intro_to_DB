#!/usr/bin/python3
"""
A Python script to create the 'alx_book_store' database in MySQL.
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",          # replace with your MySQL username
        password="#N2&,dJS2d$k@~J"  # replace with your MySQL password
    )

    if mydb.is_connected():
        cursor = mydb.cursor()
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
