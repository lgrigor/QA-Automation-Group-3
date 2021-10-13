# Insert data

import mysql.connector as mysql

db = mysql.connect(
host = "81.16.1.122",
user = "guest",
passwd = "iM9]M)bS-G",
database = "Benik_Sardaryan")

cursor = db.cursor()

data = "INSERT INTO Employees (Name, Job, City, Age, Registered) VALUES (%s, %s, %s, %s, %s)"

value = [
('Airi Sato', 'Accountant', 'Tokyo', 33, '2008/11/28'),
("Angelica Ramos", "Chief Executive Officer (CEO)", "London", 47, "2009/10/09"),
("Ashton Cox", "Junior Technical Writer", "San Francisco", 66, "2009/01/12"),
("Bradley Greer", "Software Engineer", "London", 41, "2012/10/13"),
("Brenden Wagner", "Software Engineer", "San Francisco", 28, "2011/06/07")
]

cursor.executemany(data, value)

db.commit()

print("Данные добавлены:", cursor.rowcount)
