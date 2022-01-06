# NOTE QUERIES 

# function rowcount user in ---> print(mycur.rowcout,"record inserted or deleted or updated")
# fetchall return all the rows  and fetchone returns one first row  function is used in mysql.connector

# connection_with Database mysql

s = "CREATE DATABASE mydb"
s = 'SHOW DATABASES'
s = 'CREATE TABLE mydb.custmer(name varchar(20),address(20))'
s = "Show TABLES"
s = 'CREATE TABLE custmer(id INT AUTO_INCREMENT PRIMARY KEY,name varchar(20))'
s = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
s = "ALTER TABLE customers ADD PRIMARY KEY(ID)"
s = "INSERT INTO customers (name, address) VALUES (%s, %s)"
s = "SELECT * FROM custmers"
s = "SELECT name, address FROM customers"
s = "SELECT * FROM customers WHERE address ='Park Lane 38'"
s = "SELECT * FROM customers WHERE address LIKE '%way%'" # NOTE %way% measns start or ends with %way means startwith

s1 = "SELECT * FROM customers WHERE address = %s"
a1 = ("Yellow Garden 2", )


s = "SELECT * FROM customers ORDER BY name"
s = "SELECT * FROM customers ORDER BY name DESC"

s = "DELETE FROM customers WHERE address = 'Mountain 21'"


s = "DELETE FROM customers WHERE address = %s"
a1 = ("Yellow Garden 2", )

s = "DROP TABLE customers"
s = "DROP TABLE IF EXITS custmers"

s = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

s = "UPDATE customers SET address = %s WHERE address = %s" # this is more effective that we use %s while we use the address for web hacking protection
a1 = ('Chowk Azam','Layyah') 


s = "SELECT * FROM customers LIMIT 5"
s = "SELECT * FROM customers LIMIT 5 OFFSET 2"











"""
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user = 'root,
    password = '',
    database 'mydb'   # NOTE YOU CAN CONNECT WITH DATABASE mydb
)

s = "SELECT * FROM world WHERE *someone* %LIKEYOU%"
cur= mydb.cursor() # TODO we obtain cursor object when we execute mysql query 
cur.execute(s) # NOTE executemany other function for insert many values i database



mydb.commit() # TODO for when we except the query and permanent store in database
"""

callable_iterator
