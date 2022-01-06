import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='')

cur = mydb.cursor() # NOTE if do you want to execute mysql query then make a cursor object for this..

try:
    cur.execute('DROP DATABASE haider') # create use for create database
# cur.execute('DROP DATABASE hadier') drop use for delete the database
except Exception as e:
    print("Database already exits")
