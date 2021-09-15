import mysql.connector as mysql

db = mysql.connect(
    host = "127.0.0.1",
    user = "lgrigor",
    passwd = "8zonoy",
    database = "submarine"
)
cursor = db.cursor()

## defining the Query
query = "INSERT INTO employee (emp_id, emp_name, job_name, manager_id, salary ,dep_id ) VALUES (%s, %s, %s, %s, %s, %s)"

## storing values in a variable
values = (10024, "Hadley_Sylvan", "QA_Engineer", 9523, 1250, 4)

## executing the query with values
cursor.execute(query, values)

#############cursor.execute("INSERT INTO employee (emp_id, emp_name, job_name, manager_id, salary ,dep_id ) VALUES (10024, 'Hadley_Sylvan', 'QA_Engineer', 9523, 1250, 4)")

## to make final output we have to run the 'commit()' method of the database object
db.commit()
print(cursor.rowcount, "record inserted")