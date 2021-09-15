import mysql.connector as mysql

db = mysql.connect(
    host = "127.0.0.1",
    user = "lgrigor",
    passwd = "8zonoy",
    database = "submarine"
)

cursor = db.cursor()

## creating a table called 'employee' in the 'submarine' database
cursor.execute("""CREATE TABLE employee (
    emp_id INT(5),
    emp_name VARCHAR(100),
    job_name VARCHAR(100),
    manager_id INT(4),
    salary INT(10),
    dep_id INT(1))
""")