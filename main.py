import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = '',
)

cur = mydb.cursor()

try:
    s = 'CREATE DATABASE haider1'
    cur.execute(s)
except Exception as e:
    # print('Database Already Exits ...')
    pass

try:
    # s = 'CREATE TABLE `haider1`.`student` ( `name` VARCHAR(20) NOT NULL , `age` VARCHAR(2) NOT NULL , `class` VARCHAR(12) NOT NULL , PRIMARY KEY (`age`(2))) ENGINE = InnoDB;'
    s = "CREATE TABLE haider1.student(name varchar(20),age varchar(2),class varchar(12),PRIMARY KEY(age(2)))"

    cur.execute(s)

except Exception as e:
    # print("Some thing is wrong went !")
    # print("Already Exits Please Check out !")
    pass



# s = 'INSERT INTO haider1.student(name,age,class) VALUES(%s,%s,%s)'
# b1 = (1234,'116',"haider")
# cur.execute(s,b1)
# mydb.commit()

# s = "INSERT INTO haider1.student(name,age,class) VALUES(%s,%s,%s)"
# b1=[('Haider',16,'9th A'),('Jutt',15,'9th B'),('Skillf',21,'8th A')]
# cur.executemany(s,b1)
# mydb.commit()






def display():
    s="SELECT * from haider1.student"
    cur.execute(s)
    results = cur.fetchall()
    print(results)

    # for data in results:
    #     for data1 in data:
    #         print(f"Student Name : {data1[0]}")
    #         print(f"Student Age  : {data1[1]}")
    #         print(f"Student Class: {data1[2]}")


def add():
    try:
        s = "INSERT INTO haider1.student (name,age,class) VALUES(%s,%s,%s)"
        b1 = ('Haider',15,'9th A')
        cur.execute(s,b1)
    except Exception as e:
        print("This Age already Exits Please Change the input !")


def delete():
    s = "DELETE FROM haider1.student WHERE name = 'Jutt'"
    cur.execute(s)


def search():
    s = "SELECT * FROM haider1.student WHERE age=16"
    cur.execute(s)
    result = cur.fetchall()
    print(result)



def update():
    s="UPDATE haider1.student SET class = '11th' WHERE class ='9th A' "
    cur.execute(s)


def search_name():
    s="SELECT * FROM haider1.student WHERE name = 'Haider'"
    cur.execute(s)
    results = cur.fetchall()
    print(results)





while True:
    choice = input('Please enter your choice : ')
    if choice == '1':
        display()
        print('\n\n')
    elif choice=='2':
        delete()
    elif choice=='3':
        search()
    elif choice =='4': 
        update()
    elif choice=='5':
        search_name()
    elif choice=='6':
        add()
    else:
        exit()
    mydb.commit()