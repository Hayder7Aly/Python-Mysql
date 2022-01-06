import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='haider'
    )
cur=mydb.cursor()
s="SELECT * from book"
cur.execute(s)

results = cur.fetchall()
# print(results)
j=1
for rec in results:
    # print(rec)
    rec1 = list(map(str,rec))
   
    for i in rec1:
        if len(rec1) == 1:
            print(f"{j} Data In DataBase")
        print(i)
    j+=1


input()