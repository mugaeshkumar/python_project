import mysql.connector
import datetime

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="covid_19"
    
)

mycursor=mydb.cursor()
print("1.admit patient")
print("2.view patient details")
print("3.update patient status")
print("4.view death case")
print("5.quit process")
n=int(input("enter your option:"))
if n>=6:
    print("enter correct option")
    
def add(name,age,place,admit_date,status):
    mycursor=mydb.cursor()
    sql="insert into covid19_list(name,age,place,admit_date,status) values(%s,%s,%s,%s,%s)"
    val=(name,age,place,admit_date,status)
    mycursor.execute(sql,val)
    mydb.commit()
    print("patient admitted!!!")

def view(id,name):
    mycursor=mydb.cursor()
    sql="select * from covid19_list where id=%s"%(id)
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
    
    
def update(id,name,discharge_date,status):
    mycursor=mydb.cursor()
    sql="update covid19_list set name=%s,discharge_date=%s,status=%s where id=%s"
    val=(name,discharge_date,status,id)
    mycursor.execute(sql,val)
    mydb.commit()
    print("patient status updated!!")
    
    
def death():
    mycursor=mydb.cursor()
    sql="select * from covid19_list where status='death'"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
    
if n==1:
    name=input("enter patient name:")
    age=int(input("enter patient age:"))
    place=input("enter patient location:")
    admit_date=input("enter patient admit date dd/mm/yyyy:")
    status=input("enter patient status:")
    add(name,age,place,admit_date,status)
elif n==2:
    id=int(input("enter patient ID:"))
    name=input("enter patient name:")
    view(id,name)
   
elif n==3:
    id=int(input("enter patient ID:"))
    name=input("enter patient name:")
    discharge_date=input("enter patient discharge date (dd/mm/yyyy):")
    status=input("enter patient status:")
    update(id,name,discharge_date,status)

elif n==4:
    death()
elif n==5:
    quit()
