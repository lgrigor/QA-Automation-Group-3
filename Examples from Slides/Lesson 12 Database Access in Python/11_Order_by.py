import mysql.connector as mysql

db = mysql.connect(
    host = "127.0.0.1",
    user = "lgrigor",
    passwd = "8zonoy",
    database = "submarine"
)
cursor = db.cursor()

## defining the Query
query = "SELECT * FROM employee ORDER BY emp_id"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object 
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)