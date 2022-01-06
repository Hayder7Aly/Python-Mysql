import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password = ''
)

def clear():
    from os import name,system
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

cur = mydb.cursor()

try:
    s = "CREATE DATABASE student"
    cur.execute(s)
except Exception as e:
    # print("Already Exits This Database")
    pass


try:
    s= "CREATE TABLE student.record(name varchar(20),age integer(2),class varchar(12),roll_number integer(5))"
    cur.execute(s)
    alter = "ALTER TABLE student.record ADD PRIMARY KEY(roll_number)"
    cur.execute(alter)


except Exception as e:
#     # print("Already Exits This Table")
    pass


def added():
    clear()
    try:
        name = input("Please Enter Your Name ? ")
        age = input("Please Enter Your Age :")
        clas = input("Please Enter Your Class : ")
        roll_number = input("Please Enter Your roll_number : ")
        s = "INSERT INTO student.record(name,age,class,roll_number) VALUES(%s,%s,%s,%s)"
        rec = (name,age,clas,roll_number)
        cur.execute(s,rec)
        print('Data Enter Successfully !')
    except Exception as e:
        print('Please check Your roll Number This is already exits ..')


def display():
    clear()
    s = 'SELECT * FROM student.record'
    cur.execute(s)
    result = cur.fetchall()
    # print(result)

    name,age,clas1,roll_number = 'Student Name'.center(12),"Studnet Age".center(24),"Student Class".center(36),"Roll Number".center(48)
    print(name,age,clas1,roll_number)
    for row in result:
        new = f"{row[0]}".center(12)
        age = f"{row[1]}".center(24)
        clas1 = f"{row[2]}".center(36)
        roll = f"{row[3]}".center(48)
        
        print(new,age,clas1,roll)

def search():
    clear()
    roll_no = input('Please Enter Your Roll number : ')
    s = f"SELECT * FROM student.record WHERE roll_number = {roll_no}"
    cur.execute(s)
    result = cur.fetchall()
    if result == []:
        print("This Roll Number Not Exits In Data")
    else:
        print(result)

def delete():
    # try:
    roll_number=int(input("Please enter the Roll number of students : "))
    s = 'SELECT * FROM student.record'
    cur.execute(s)
    res = cur.fetchall()
    for row in res:
        if roll_number in row:
            s = f"DELETE FROM student.record WHERE roll_number = '{roll_number}'"
            cur.execute(s)
            print(f'This roll number data {roll_number} is deleted completely And Student Name is {row[0]} !')
            break
    else:
        print("This Rollno not exits in data ..")
  
def update():
    roll_number1 = int(input("Please Enter the Roll Number Of Student : "))
    clear()
    name = input("PLEASE ENTER THE NAME OF STUDENT : ")
    # age = int(input("PLEASE ENTER THE AGE OF STUDENT : "))
    # clas1 = input('PLEASE ENTER THE CLASS OF STUDNET : ')
    # roll_number = int(input('PLEASE ENTER THE ROLL NUMBER OF STUDENT : '))
    s = f"UPDATE student.record SET name = {name} WHERE roll_number = {roll_number1}"
    cur.execute(s)


def search_name():
    clear()
    name = input('Please Enter the name of student : ')
    s = 'SELECT * FROM student.record'
    cur.execute(s)
    result = cur.fetchall()
    for row in result:
        if name in row :
            print(f'Student Roll Number = {row[3]}')
            print(f"Student Class Name  = {row[2]}")


            
if __name__ == "__main__":
    while True:
        choice = input('Please Enter Your choice : ')
        if choice == '1':
            added()
        elif choice=='2':
            display()
        elif choice =='3':
            search()
        elif choice=='4':
            delete()
        elif choice == '5':
            update()
        elif choice == '6':
            search_name()
        else:
            exit()
        mydb.commit()