import mysql.connector as mysql
db = mysql.connect(
    host = "81.16.1.122",
    user = "guest",
    passwd = "iM9]M)bS-G",
    database = "Yelena_Manukyan"
)

cursor = db.cursor()
#cursor.execute("CREATE DATABASE Yelena_Manukyan")
#cursor.execute("SHOW DATABASES")
#databases = cursor.fetchall()
#print(databases)
#for database in databases:
    #print(database)

#cursor.execute("""CREATE TABLE employee (
    #emp_name VARCHAR(100),
    #emp_position VARCHAR(100),
    #emp_city VARCHAR(100),
    #emp_age INT,
    #emp_StJob VARCHAR(50))
#""")
#cursor.execute("SHOW TABLES")
#tables =  cursor.fetchall()
#for table in tables:
    #print(table)

"""query = "INSERT INTO employee (emp_name, emp_position, emp_city, emp_age, emp_StJob) VALUES (%s, %s, %s, %s, %s)"
values = (("Airi Sato", "Accountant", "Tokyo", 33, "2008/11/28"),
("Angelica Ramos", "Chief Executive Officer (CEO)", "London", 47, "2009/10/09"),
("Ashton Cox", "Junior Technical Writer", "San Francisco", 66, "2009/01/12"),
("Bradley Greer", "Software Engineer", "London", 41, "2012/10/13"),
("Brenden Wagner", "Software Engineer", "San Francisco", 28, "2011/06/07"))"""

"""cursor.executemany(query, values)
db.commit()
print(cursor.rowcount,"record inserted")"""

"""query = "SELECT * FROM employee"
cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)"""

"""query = "DELETE FROM employee WHERE emp_position = 'Software Engineer' "
cursor.execute(query)
db.commit()"""

"""query = "SELECT * FROM employee WHERE emp_StJob REGEXP '/10/' ORDER BY emp_name DESC"
cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)"""





