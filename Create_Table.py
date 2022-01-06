import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='haider'
    )
cur = mydb.cursor()

# for NOTE ENGINE = InnoDB;

s="CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,2))"

cur.execute(s)