# Create table

import mysql.connector as mysql

db = mysql.connect(
host = "81.16.1.122",
user = "guest",
passwd = "iM9]M)bS-G",
database = "Benik_Sardaryan")

cursor = db.cursor()

cursor.execute("CREATE TABLE Employees (Name VARCHAR(255), Job VARCHAR(255), City VARCHAR(255), Age INT, Registered DATE)")
