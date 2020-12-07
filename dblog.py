import mysql.connector
import tkinter
from tkinter import *
from prettytable import PrettyTable
from tkinter import messagebox
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='users')
mycur=mydb.cursor()
while(True):
    print("####################Course Management System########################\n")
    print("Select the operation you want to perform:\n")
    s=int(input("1.SignUp\n2.Course Details\n3.Availabity of courses and Registeration\n4.User Existance\n5.Exit\n"))
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
                messagebox.showinfo("Course Management System","User Has Signed Up Successfully!!!")
        root = Tk()
        root.geometry('540x600')
        root.configure(background="white")
        labelframe = LabelFrame(root, text="Registeration Form",bd=30,fg="black",font=("italic",35,"bold"),bg="Peachpuff",highlightthickness=20)
        labelframe.pack(fill="both",expand="yes")
        root.title("Registration Form")
        label_email = Label(root, text="Username:",width=10,font=("courier", 14,"bold"),fg="black",bg="white")
        label_email.place(x=120,y=170)
        a= Entry(root,width=25,bd=5,bg="lightblue2",fg="white")
        a.place(x=280,y=170)
        label_uname = Label(root, text="City:   ",width=10,font=("courier", 14,"bold"),fg="black",bg="white")
        label_uname.place(x=120,y=230)
        b= Entry(root,width=25,bd=5,bg="lightblue2",fg="white")
        b.place(x=280,y=230)
        label_uname = Label(root, text="Age:    ",width=10,font=("courier", 14,"bold"),fg="black",bg="white")
        label_uname.place(x=120,y=280)
        c= Entry(root,width=25,bd=5,bg="lightblue2",fg="white")
        c.place(x=280,y=280)
        Button(root, text='Submit',width=20,font=("bold",12),bg='skyblue',fg='white',command=getv).place(x=170,y=410)
        root.mainloop()
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
            print("User Has Successfully Registered On Selected Course!!!\n")
    if(s==4):
        print("****************User Registeration*****************")
        nam=input("enter the username:\n")
        sql=("SELECT Username FROM Signup where Username=%s")
        Username=[nam,]
        mycur=mydb.cursor()
        mycur.execute(sql,Username)
        r=mycur.fetchall()
        for i in r:
            st=''.join(i)
            if(st==nam):
                print("User Already Registered\n")
                break
        else:
            print("User Does Not Exist Please SignUp First!!!\n")
    if(s==5):
        exit()
