import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='')

# print(mydb) NOTE that returns object that is not callable

print(mydb.connection_id) # TODO if it returns id then we are connect with database