import mysql.connector as mysql

db = mysql.connect(
    host = "127.0.0.1",
    user = "lgrigor",
    passwd = "8zonoy",
    database = "submarine"
)
cursor = db.cursor()

## defining the Query
query = "SELECT emp_id, emp_name FROM employee"

## getting 'emp_id, emp_name' columns from the table 
cursor.execute(query)

## fetching all usernames from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records :
    print(record)
