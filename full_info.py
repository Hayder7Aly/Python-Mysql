import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='haider'
)

cur = mydb.cursor()

# s='CREATE DATABASE haider'
# s = 'SHOW DATABASES' for show the databases
# s='DROP DATABASE haider'
# s="CREATE TABLE student(name varchar(20), age integer)"
# s="INSERT INTO student(name, age) VALUES(%s,%s)"
# b1 = [
#     ('HAIDER Ali',16),
#     ('Ali Raza',20),
#     ('Asad',15),
#     ('Farman',23)
# ]
# cur.executemany(s,b1)

# s='TRUNCATE TABLE student'


# cur.execute("SELECT *FROM student")
# for i in cur:
#     print(i)

# list_of_data = cur.fetchall()
# for row in list_of_data:
#     for item in row:
#         print(item)






# print(cur.fetchall()) # that returns a list with inside name in  tuple 

# for name in cur: # show databases
#     for i in name:
#         print(i)


# s='DROP DATABASE mydb1'
# cur.execute(s)

s="INSERT INTO student(roll_no,name,age) VALUES(%s,%s,%s)"
stud=[(1,"Haider Ali 123",16),(2,'Ali Raza',20)]
cur.executemany(s,stud)
mydb.commit()
mydb.close()