import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="atm_mechine"
)

mycursor=mydb.cursor()
print("\t\t1.create account")
print("\t\t2.view account details")
print("\t\t3.withdraw and deposit amount")
print("\t\t4.change pin")
print("\t\t5.quit process")
n=int(input("enter your option:"))

if n>=6:
 print("please enter correct option")  
account_num =""
name=""
amount=""
pin=""

if n==1:
    acc_num=int(input("enter your account number:"))
    hol_nam=input("enter your name:")
    amt=int(input("enter your initial amount:"))
    u_pin=int(input("set your new pin:"))
    print("data insert")
    account_num=acc_num
    name=hol_nam
    amount=amt
    pin=u_pin
    
    sql="insert into atm_mechine(account_num,name,amount,pin) value(%s,%s,%s,%s)"
    val=(account_num,name,amount,pin)
    mycursor.execute(sql,val)
    mydb.commit()
    
elif n==2:
    acc_num=int(input("enter your account number:"))
    u_pin=int(input("enter your pin:"))
    account_num=acc_num
    pin=u_pin
    sql="select * from atm_mechine where pin='%s'" %(u_pin)
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for i in myresult:
        print(i)
        
elif n==3:
    acc_num=int(input("enter your account number:"))
    u_pin=int(input("enter your pin:"))
    mycursor=mydb.cursor()
    mycursor.execute("select * from atm_mechine where account_num='%s'"%(acc_num))
    row=mycursor.fetchone()
    if mycursor.rowcount ==1:
        
        mycursor.execute("select * from atm_mechine where pin='%s'"%(u_pin))
        row=mycursor.fetchone()
        if mycursor.rowcount ==1:
            print("login successful")
            d=int(input("enter 1 for withdraw or 2 for deposit & 3 for exit:"))
            if d==1:
                a=int(input("enter your withdraw amount:"))
                mycursor.execute("select amount from atm.mechine where pin='%s'"%(u_pin))
                result=mycursor.fetchone()
                x=list(result)
                for i in x:
                    z=(int(i))
                    c=z-a
                mycursor.execute("update atm_mechine set amount='%s'where pin='%s'"%(c,u_pin))
                print("amount withdrawl!!")
            if d==2:
                a=int(input("enter your deposite amount:"))
                mycursor.execute("select amount from atm_mechine where pin='%s'"%(u_pin))
                result=mycursor.fetchone()
                x=list(result)
                for i in x:
                    z=(int(i))
                    c=z+a
                mycursor.execute("update atm_mechine set amount='%s'where pin='%s'"%(c,u_pin))
                print("amount deposited")
            if d==3:
                exit(0)
                
        else:
            print("invalid pin")
            
    else:
        print("account doesn't exist")
    mydb.commit()    
    
    
elif n==4:
    acc_num=int(input("enter your account number:"))
    u_pin=int(input("enter your pin:"))
    mycursor=mydb.cursor()
    mycursor.execute("select * from atm_mechine where account_num='%s'"%(acc_num))
    row=mycursor.fetchone()
    if mycursor.rowcount ==1:
        
        mycursor.execute("select * from atm_mechine where pin='%s'"%(u_pin))
        row=mycursor.fetchone()
        if mycursor.rowcount ==1:
         new_pin=int(input("enter your new pin:"))
         mycursor.execute("update atm_mechine set pin='%s'where pin='%s'" %(new_pin,u_pin))
         print("pin successfully changed!!")
        else:
            print("invalid pin!!!")
            
    else:
        print("account does't exist!!")
    mydb.commit()

elif n==5:
    quit()
    
        
                 
                 
                
    
        
            