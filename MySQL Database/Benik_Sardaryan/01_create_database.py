# Create DB

import mysql.connector as mysql

db = mysql.connect(
host = "81.16.1.122",
user = "guest",
passwd = "iM9]M)bS-G")

cursor = db.cursor()

cursor.execute("CREATE DATABASE Benik_Sardaryan")
