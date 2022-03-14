# Show DB

import mysql.connector as mysql

db = mysql.connect(
host = "IP Address",
user = "guest",
passwd = "iM9]M)bS-G")

cursor = db.cursor()

cursor.execute("SHOW DATABASES")
db = cursor.fetchall()


for database in db:
    print(database)
