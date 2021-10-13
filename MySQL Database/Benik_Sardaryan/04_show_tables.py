# Show tables

import mysql.connector as mysql

db = mysql.connect(
host = "81.16.1.122",
user = "guest",
passwd = "iM9]M)bS-G",
database = "Benik_Sardaryan")

cursor = db.cursor()

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()


for table in tables:
    print(table)
