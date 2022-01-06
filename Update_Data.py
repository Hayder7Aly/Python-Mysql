import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='haider'
    )
cur = mydb.cursor()
s = "UPDATE book SET price=price+10 WHERE price=555"
cur.execute(s)
mydb.commit()