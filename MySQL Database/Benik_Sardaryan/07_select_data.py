# Delete lines in table

import mysql.connector as mysql

db = mysql.connect(
host = "IP Address",
user = "guest",
passwd = "iM9]M)bS-G",
database = "Benik_Sardaryan")

cursor = db.cursor()

sel_data = "SELECT * FROM Employees WHERE Registered LIKE '%-10-%'"

cursor.execute(sel_data)

data = cursor.fetchall()

for month in data:
    print(month)
