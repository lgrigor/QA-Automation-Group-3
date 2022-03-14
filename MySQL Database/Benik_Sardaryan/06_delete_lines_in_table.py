# Delete lines in table

import mysql.connector as mysql

db = mysql.connect(
host = "IP Address",
user = "guest",
passwd = "iM9]M)bS-G",
database = "Benik_Sardaryan")

cursor = db.cursor()

soft_eng_del = "DELETE FROM Employees WHERE Job = 'Software Engineer'"

cursor.execute(soft_eng_del)

db.commit()

print("Удалено данных:", cursor.rowcount)
