import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="bus_ticket"
)

mycursor=mydb.cursor()
print("1.Booking ticket")
print("2.Changing ticket ")
print("3.view your ticket")
print("4.cancel your ticket")
print("5.quit process")
n=int(input("enter your option:"))
if n>=6:
    print("enter correct option")
    
def book_ticket(name,start,stop):
    mycursor=mydb.cursor()
    sql="insert into onbus_ticket(name,start,stop) values(%s,%s,%s)"
    val=(name,start,stop)
    mycursor.execute(sql,val)
    mydb.commit()
    print("your ticket is booked!!")
    
def change_ticket(name,start,stop,id):
    mycursor=mydb.cursor()
    sql="update onbus_ticket set name=%s,start=%s,stop=%s where id=%s"
    val=(name,start,stop,id)
    mycursor.execute(sql,val)
    mydb.commit()
    print("your ticket changed successfully")
    
def view_ticket(id):
    mycursor=mydb.cursor()
    sql="select * from onbus_ticket where id=%s"%(id)
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for i in myresult:
        print(i)

def cancel_ticket(id):
    mycursor=mydb.cursor()
    sql="delete from onbus_ticket where id=%s"%(id)
    mycursor.execute(sql)
    mydb.commit()
    print("your ticket is canceled")


if n==1:
    name=input("enter your name:")
    start=input("enter your journey from:")
    stop=input("enter your journey to:")
    book_ticket(name,start,stop)

elif n==2:
    id=(input("enter your id:"))
    name=input("enter your name:")
    start=input("enter your journey from:")
    stop=input("enter your journey to:")
    change_ticket(name,start,stop,id)
    
elif n==3:
    id=(input("enter your id:"))
    name=input("enter your name:")
    view_ticket(id)
    
elif n==4:
    id=input("enter your id:")
    name=input("enter your name:")
    cancel_ticket(id)

elif n==5:
    quit()
    
