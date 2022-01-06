import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='haider'
    )

cur = mydb.cursor()

s = "INSERT INTO book(bookid,title,price) VALUES(%s,%s,%s)"

books=[(1,'Python3',999),(2,'Java8',245),(3,'HTML',555),(4,'CSS',870)]

cur.executemany(s,books)

mydb.commit()