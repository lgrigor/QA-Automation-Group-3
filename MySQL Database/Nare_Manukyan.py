import mysql.connector as mysql

db = mysql.connect(
   host = "IP Address change to IP Address",
   user = "guest",
   passwd = "iM9]M)bS-G",
   database = "Nare_Manukyan"
)
cursor = db.cursor()

# Create table Employee

# cursor.execute("""CREATE TABLE Employee (
#     Name VARCHAR(30),
#     Job VARCHAR(30),
#     City VARCHAR(30),
#     Age INT,
#     HireDate VARCHAR(30))
# """)

# Insert the bottom lines at once

# query = "INSERT INTO Employee(Name, Job, City, Age, HireDate)" \
#         "VALUES (%s, %s, %s, %s, %s)"
# Values = [
#     ("Airi Sato", 'Accountant', 'Tokyo', 33, '2008/11/28'),
#     ("Angelica Ramos", "Chief Executive Officer (CEO)", "London", 47, "2009/10/09"),
#     ("Ashton Cox", "Junior Technical Writer", "San Francisco", 66, "2009/01/12"),
#     ("Bradley Greer", "Software Engineer", "London", 41, "2012/10/13"),
#     ("Brenden Wagner", "Software Engineer", "San Francisco", 28, "2011/06/07")
# ]
# cursor.executemany(query, Values)
# db.commit()
# query = "SELECT * FROM Employee"
# cursor.execute(query)
# values = cursor.fetchall()
# print(values)

#  Delete the lines that contain the word "software engineer"

delete_lines = "DELETE FROM Employee WHERE Job = 'software engineer'"
cursor.execute(delete_lines)
db.commit()
lines = "SELECT * FROM Employee WHERE MONTH(HireDate) = 10"
cursor.execute(lines)
records = cursor.fetchall()
print(records)
