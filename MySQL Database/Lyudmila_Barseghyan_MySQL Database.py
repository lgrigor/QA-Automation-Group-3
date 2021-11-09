import mysql.connector as mysql


db = mysql.connect(
    host = "81.16.1.122",
    user = "guest",
    passwd= "iM9]M)bS-G",
    database= "lyudmila_barseghyan"
)

cursor = db.cursor()
cursor.execute("""CREATE TABLE employee (
    emp_name VARCHAR(100),
    job_name VARCHAR(100),
    city VARCHAR(100),
    age INT,
    work_from VARCHAR(100))
""")

query = "INSERT INTO employee (emp_name, job_name, city, age, work_from) VALUES (%s, %s, %s, %s, %s)"
values = [
    ('Airi Sato', 'Accountant', 'Tokyo', 33, '2008/11/28'),
    ("Angelica Ramos", "Chief Executive Officer (CEO)", "London", 47, "2009/10/09"),
    ("Ashton Cox", "Junior Technical Writer", "San Francisco", 66, "2009/01/12"),
    ("Bradley Greer", "Software Engineer", "London", 41, "2012/10/13"),
    ("Brenden Wagner", "Software Engineer", "San Francisco", 28, "2011/06/07")

]
cursor.executemany(query, values)
db.commit()
query = "SELECT * FROM employee"
cursor.execute(query)
records = cursor.fetchall()

for record in records:
    print(record)


print('--------------------------------------------------')
del_query = "DELETE FROM employee WHERE job_name = 'Software Engineer'"
cursor.execute(del_query)
db.commit()


query = "SELECT * FROM employee"
cursor.execute(query)
records = cursor.fetchall()

for record in records:
    print(record)


print('--------------------------------------------------')

query = "SELECT * FROM employee WHERE work_from REGEXP '10'"
cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)

print('--------------------------------------------------')

