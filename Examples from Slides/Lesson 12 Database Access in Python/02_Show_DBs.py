import mysql.connector as mysql

db = mysql.connect(
    host = "127.0.0.1",
    user = "lgrigor",
    passwd = "8zonoy"
)

cursor = db.cursor()

## executing the statement using 'execute()' method
cursor.execute("SHOW DATABASES")

## 'fetchall()' method fetches all the rows from the last executed statement
databases = cursor.fetchall() ## it returns a list of all databases present

## printing the list of databases
print(databases)

## showing one by one database
for database in databases:
    print(database)
