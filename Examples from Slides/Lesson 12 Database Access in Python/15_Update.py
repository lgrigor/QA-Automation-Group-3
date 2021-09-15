import mysql.connector as mysql

db = mysql.connect(
    host = "127.0.0.1",
    user = "lgrigor",
    passwd = "8zonoy",
    database = "submarine"
)
cursor = db.cursor()

## defining the Query
query = "UPDATE employee SET emp_name = 'Kareem_Sylvan' WHERE emp_id = 10024"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()