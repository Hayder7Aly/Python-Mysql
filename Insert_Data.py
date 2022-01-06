import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='haider'
)

cur = mydb.cursor()
s="INSERT INTO book(bookid,title,price) VALUES(%s,%s,%s)"
b1=(11,'Java',115)
cur.execute(s,b1)
mydb.commit() # this is used for save the database with some task ..