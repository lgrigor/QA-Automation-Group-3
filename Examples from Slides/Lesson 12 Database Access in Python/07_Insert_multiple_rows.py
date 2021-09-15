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
values = [
(10037, "Marcie_Elodie", "RnD_Engineer", 9012, 1500, 4),
(10164, "Eileen_Candi", "RnD_Engineer", 9012, 1500, 4),
(10021, "Floretta_Ike", "QA_Engineer", 9523, 750, 4),
(10094, "Gideon_Talia", "QA_Engineer", 9567, 500, 5)
]
## executing the query with values
cursor.executemany(query, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()
print(cursor.rowcount, "record inserted")