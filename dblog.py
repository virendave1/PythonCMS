import mysql.connector
import tkinter
from tkinter import *
from prettytable import PrettyTable
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='users')
mycur=mydb.cursor()
while(True):
    print("####################Course Management System########################\n")
    print("Select the operation you want to perform:\n")
    s=int(input("1.Registeration\n2.Course Details\n3.Availabity of courses\n4.User Existance\n5.Exit\n"))
    if(s==1):
        def getv():
            m=a.get()
            n=b.get()
            l=c.get()
            l=str(l)
            if(m!=""):
                n=[m,n,l]
                sql=("insert  into Signup(Username,City,Age) values(%s,%s,%s)")
                mycur.execute(sql,n)
                mydb.commit()
                tkinter.Label(f,text="User has been Successfully Registered!!! ",fg="gold",bg="black").grid(row=9,column=2)
        f=tkinter.Tk()
        f.title("Student Registeration Form")
        f.configure(background='yellow')        
        ll=tkinter.Label(f,text="**************REGISTERATION FORM*****************",fg="red",bg="pink").grid(row=1,column=2,padx=6,pady=6)
        a1=tkinter.Label(f,text="Name:",fg="red",bg="pink").grid(row=3,column=1,padx=4,pady=6)
        b1=tkinter.Label(f,text="City:",fg="red",bg="pink").grid(row=4,column=1,padx=4,pady=6)
        c1=tkinter.Label(f,text="Age:",fg="red",bg="pink").grid(row=5,column=1,padx=4,pady=6)
        a=tkinter.StringVar()
        b=tkinter.StringVar()
        c=tkinter.IntVar()
        a_e=tkinter.Entry(f,textvariable=a,bg="tan1",fg="white").grid(row=3,column=2,padx=4,pady=6)
        b_e=tkinter.Entry(f,textvariable=b,bg="tan1",fg="white").grid(row=4,column=2,padx=4,pady=6)
        c_e=tkinter.Entry(f,textvariable=c,bg="tan1",fg="white").grid(row=5,column=2,padx=4,pady=6)
        tkinter.Button(f,text="Submit",command=getv).grid(padx=15,pady=10,row=7,column=2)          
    if(s==2):
        print("***************Course Details*****************")
        sql=("select * from coursedetails")
        mycur.execute(sql)
        ress=[]
        ress=mycur.fetchall()
        
        tab=PrettyTable(['Course-Name','Fees','Duration'])
        for i in range(0,6):
            tab.add_row(ress[i])
        print(tab)
    if(s==3):
        print("*************check available courses*************\n")
        sql=("select * from courses")
        mycur.execute(sql)
        ress=[]
        ress=mycur.fetchall()
        tab1=PrettyTable(['Available-course'])
        for i in range(0,6):
            tab1.add_row(ress[i])
        print(tab1)
        t=int(input("select the course you want to register:\n"))
        if(t==1):
            username=input("enter the username\n")
            course="programming"
            n=[username,course]
            sql=("insert  into courseregisteration(username,course) values(%s,%s)")
            mycur.execute(sql,n)
            mydb.commit()
            print("user has successfully registered on selected course!!!\n")
        if(t==2):
            username=input("enter the username\n")
            course="web-development"
            n=[username,course]
            sql=("insert  into courseregisteration(username,course) values(%s,%s)")
            mycur.execute(sql,n)
            mydb.commit()
            print("user has successfully registered on selected course!!!\n")
        if(t==3):
            username=input("enter the username\n")
            course="android-development"
            n=[username,course]
            sql=("insert  into courseregisteration(username,course) values(%s,%s)")
            mycur.execute(sql,n)
            mydb.commit()
            print("user has successfully registered on selected course!!!\n")
        if(t==4):
            username=input("enter the username\n")
            course="cloud-computing"
            n=[username,course]
            sql=("insert  into courseregisteration(username,course) values(%s,%s)")
            mycur.execute(sql,n)
            mydb.commit()
            print("user has successfully registered on selected course!!!\n")
        if(t==5):
            username=input("enter the username\n")
            course="database-management"
            n=[username,course]
            sql=("insert  into courseregisteration(username,course) values(%s,%s)")
            mycur.execute(sql,n)
            mydb.commit()
            print("user has successfully registered on selected course!!!\n")
        if(t==6):
            username=input("enter the username\n")
            course="network & security"
            n=[username,course]
            sql=("insert  into courseregisteration(username,course) values(%s,%s)")
            mycur.execute(sql,n)
            mydb.commit()
            print("user has successfully registered on selected course!!!\n")
    if(s==4):
        print("****************User Registeration*****************")
        nam=input("enter the username:\n")
        sql=("SELECT Username FROM signup where Username=%s")
        Username=[nam,]
        mycur=mydb.cursor()
        mycur.execute(sql,Username)
        r=mycur.fetchall()
        for i in r:
            st=''.join(i)
            if(st==nam):
                print("user already registered\n")
                break
        else:
            print("user has not registered any course please register the course you want!!!\n")
    if(s==5):
        exit()
