import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='haider1'
)

cur=mydb.cursor()

# s="DELETE FROM book" # that delete all the content from the table 
s="DELETE FROM student WHERE name = 'HTML'"

cur.execute(s)
mydb.commit()