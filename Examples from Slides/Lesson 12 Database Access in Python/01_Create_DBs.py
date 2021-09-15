import mysql.connector as mysql

db = mysql.connect(
    host = "127.0.0.1",
    user = "lgrigor",
    passwd = "8zonoy"
)

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

## creating a databse called 'submarine'
## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create the 'submarine' database cursor.execute("CREATE DATABASE submarine")
cursor.execute("CREATE DATABASE submarine")