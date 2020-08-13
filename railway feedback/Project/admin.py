from tkinter import *
from sqlite3 import *
from tkinter import messagebox
from twilio.rest import Client
import random,re
from PIL import ImageTk,Image
import requests, json

class Mygui():
    def __init__(s):
        s.apna_Admin()
    def getrecordsAdmin(s,m):
        m.destroy()
        c=connect("inr.db")
        cur=c.cursor()
        x=cur.execute("select * from feedback")
        y=0
        t=0
        for i in x:
            n=i[:-1]
            n=n[1:]
            y+=sum(n)
            t+=1
        try:
            avg=y/t
            avg=avg/13
            avg=(avg/5)*100
        except:
            avg=0
        m=cur.execute("select count(*) from feedback")
        scr=Tk()
        scr.geometry('1400x1400+0+0')
        img=PhotoImage(file="railways.png")
        l=Label(scr,image=img)
        l.place(x=0,y=0)
        l1=Label(scr,text="Welcome to Admin Portal ",font=("times",30,"bold"))
        l1.place(x=500,y=30)
        l2=Label(scr,text="Average",font=("times",30,"bold"))
        l2.place(x=500,y=300)
        l3=Label(scr,text="%f"%avg,font=("times",30,"bold"))
        l3.place(x=700,y=300)
        l4=Label(scr,text="Number of feedback %d"%m.fetchone()[0],font=("times",30,"bold"))
        l4.place(x=450,y=400)

        scr.mainloop()
        
    def delrecordsAdmin(s):
        c=connect("inr.db")
        cur=c.cursor()
        x=cur.execute("delete from feedback")
        c.commit()
        messagebox.showinfo("Admin","all records erased")
    def task(s):
        scr=Tk()
        scr.geometry('1400x1400+0+0')
        img=PhotoImage(file="railways.png")
        l=Label(scr,image=img)
        l.place(x=0,y=0)
        l1=Label(scr,text="Welcome to Admin Portal ",font=("times",30,"bold"))
        l1.place(x=500,y=30)
        b=Button(scr,text="Click here to get records",font=("times",30,"bold"),command=lambda :s.getrecordsAdmin(scr))
        b.place(x=500,y=300)
        b1=Button(scr,text="Click here to reset records",font=("times",30,"bold"),command=s.delrecordsAdmin)
        b1.place(x=500,y=500)
        scr.mainloop()


    def login(s,ui,username,password):
        if len(username) and len(password):
            x=s.c.execute("select count(*) from users where name=%r and password=%r"%(username,password))
            if list(x)[0][0]!=0:
                ui.destroy()
                s.task()
            else:
                messagebox.showinfo("Admin login","incorrect credentials")
        else:
            messagebox.showinfo("Admin login","please enter user name and password")
    def register(s,ui,n,pass1,pass2,email):
        if len(n) and len(pass1) and len(pass2) and len(email):
            if pass1==pass2:
                if re.search(r"\w+@+\w+.+\w",email):
                    try:
                        s.c.execute("insert into users values(%r,%r,%r)"%(n,pass1,email))
                        s.con.commit()
                    except:
                        messagebox.showinfo("Admin login","username all ready exists")
                    else:
                        ui.destroy()
                        s.apna_Admin()
                else:
                    messagebox.showinfo("Admin login","invalid email")
            else:
                messagebox.showinfo("Admin login","incorrect password")
        else:
            messagebox.showinfo("Admin login","please all field")


    def registerpage(s,ui):
        ui.destroy()
        scr=Tk(className="Admin")
        scr.geometry('800x600+0+0')
    ##    p=PhotoImage(file="minion.png")
    ##    l=Label(scr,image=p)
    ##    l.grid(row=0,column=0)
        lab=Label(scr,text="Register Page",font=("times",30,"underline"))
        lab.place(x=250,y=40)
        u=Label(scr,text="User Name",font=("times",20,"underline"))
        u.place(x=100,y=200)
        pa=Label(scr,text="Password",font=("times",20,"underline"))
        pa.place(x=100,y=250)
        pa1=Label(scr,text="Retype Password",font=("times",20,"underline"))
        pa1.place(x=100,y=300)
        el=Label(scr,text="email",font=("times",20,"underline"))
        el.place(x=100,y=350)
        user=Entry(scr,font=("times",20,"bold"))
        user.place(x=300,y=200)
        pas=Entry(scr,font=("times",20,"bold"),show="*")
        pas.place(x=300,y=250)
        pas1=Entry(scr,font=("times",20,"bold"),show="*")
        pas1.place(x=300,y=300)
        email=Entry(scr,font=("times",20,"bold"))
        email.place(x=300,y=350)
        b1=Button(scr,text="Register",font=("times",20,"italic"),command=lambda :s.register(scr,user.get(),pas.get(),pas1.get(),email.get()))
        b1.place(x=300,y=400)
        scr.mainloop()

    def apna_Admin(s):
            #database
        s.con=connect("user.db")
        s.c=s.con.cursor()
        try:
           s.c.execute("create table data(name varchar(500),price varchar(50),ptag float,site varchar(50))")
           s.c.execute("create table users(name varchar(20) UNIQUE,password varchar(20),email varchar(50))")
        except:
            pass
        #main screen
        scr=Tk(className="Admin Pannel Login")
        scr.geometry('800x600+0+0')
##        p=PhotoImage(file="")
##        l=Label(scr,image=p)
##        l.grid(row=0,column=0)
        lab=Label(scr,text="LOGIN Page",font=("times",30,"underline"))
        lab.place(x=250,y=40)
        u=Label(scr,text="User Name",font=("times",20,"underline"))
        u.place(x=100,y=250)
        pa=Label(scr,text="Password",font=("times",20,"underline"))
        pa.place(x=100,y=300)
        user=Entry(scr,font=("times",20,"bold"))
        user.place(x=300,y=250)
        pas=Entry(scr,font=("times",20,"bold"),show="*")
        pas.place(x=300,y=300)
        b=Button(scr,text="Login",font=("times",20,"italic"),command=lambda :s.login(scr,user.get(),pas.get()))
        b.place(x=100,y=350)
        b1=Button(scr,text="Register",font=("times",20,"italic"),command=lambda :s.registerpage(scr))
        b1.place(x=300,y=350)
        scr.mainloop()

global var
def msg(a,b,c,d,x,y):
    x=re.search(r'\d+',x)
    if x!=None:
        x=x.string
    else:
        x=''
    d=re.search(r'\S+@\w+[.]\w{2,3}',d)
    if d==None:
        messagebox.showinfo("INR","Enter A valid email")
    try:
        if(len(x)!=10):
            messagebox.showinfo("INR","Enter A Valid Mobile Number")
        y.destroy()
    except:
        pass
    if len(x)==10:
        otp=random.randint(1000,9999)
        account_sid = "AC202680080586a621aa22f8c185335a6c"
        auth_token = "30618cde6069ba63cbb873b33930aa29"
        client = Client(account_sid, auth_token)
        client.messages.create(to="+91"+x,from_="+18653442353",body="Welcome to Indian Northen Railway your otp is %d"%otp)
        scr=Tk(className="Railway Feedback Form")
        f=Frame(scr)
        f.pack(fill=BOTH,expand=1)
        l=Label(f,text="Enter A Valid MOBILE NUMBER",font=("times",20,"bold"))
        l.pack(fill=X,side=TOP)
        e=Entry(f,font=("times",18))
        e.pack()
        e.insert(0,x)
        l1=Label(f,text="Enter otp",font=("times",20,"bold"))
        l1.pack(fill=X,side=TOP)
        e1=Entry(f,font=("times",18))
        e1.pack()
        b=Button(f,text="Submit",font=("times",20,"bold"),command=lambda :valid(e.get(),otp,e1.get(),scr))
        b1=Button(f,text="Resend otp",font=("times",20,"bold"),command=lambda :msg(e.get(),scr))
        b.pack()
        b1.pack()
        scr.mainloop()
    else:
        home()
        

def valid(x,a,b,y):
    global var
    if(len(x)!=10):
        messagebox.showinfo("INR","Enter A Valid Mobile Number")
    y.destroy()
    if (len(x)!=10)and(str(a)!=b):
        home()
    if len(x)==10 and (str(a)==b):
        var=x
        forms()
def home():
    scr1=Tk(className="Railway Feedback Form")
    f=Frame(scr1)
    f.pack(fill=BOTH,expand=1)
    l=Label(f,text="Passenger Name",font=("times",20,"bold"))
    l.pack(fill=X,side=TOP)
    ep=Entry(f,font=("times",18))
    ep.pack()
    l=Label(f,text="City",font=("times",20,"bold"))
    l.pack(fill=X,side=TOP)
    ec=Entry(f,font=("times",18))
    ec.pack()
    l=Label(f,text="State",font=("times",20,"bold"))
    l.pack(fill=X,side=TOP)
    es=Entry(f,font=("times",18))
    es.pack()
    l=Label(f,text="E-Mail ID",font=("times",20,"bold"))
    l.pack(fill=X,side=TOP)
    ee=Entry(f,font=("times",18))
    ee.pack()
##    def print_var(*_):
##        print(option.get())
##    v = IntVar()
##    l=Label(f,text="Gender",font=("times",20,"bold"))
##    l.pack(fill=X,side=TOP)
##    R1=Radiobutton(text="Male", variable=v, value=1).pack(anchor=W)
##    R2=Radiobutton(text="Female", variable=v, value=2).pack(anchor=W)
    l=Label(f,text="Enter A Valid MOBILE NUMBER",font=("times",20,"bold"))
    l.pack(fill=X,side=TOP)
    em=Entry(f,font=("times",18))
    em.pack()
    b=Button(f,text="Submit",font=("times",20,"bold"),command=lambda :msg(ep.get(),ec.get(),es.get(),ee.get(),em.get(),scr1))
    b.pack()
    scr1.mainloop()
def addrecord(x,*a):
    global var
    x.destroy()
    con=connect("inr.db")
    cur=con.cursor()
    try:
        cur.execute("create table feedback(pnr int not null UNIQUE,tw int,tf int,tm int,twb int,smell int,smellmos int,cc int,cd int,cv int,ca int,cvf int,bw int,hyg int,stais varchar(5))")
    except:
        pass
    cur.execute("insert into feedback values({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},'{14}')".format(int(var),*list(map(int,a[:-1])),a[-1]))
    con.commit()
    con.close()
    messagebox.showinfo("Indian Railway",'Thank You  for your feedback submitted sucessfully!!!')

    
def forms():
    scr=Tk(className="Railway Feedback Form")
    img=PhotoImage(file="")
    l=Label(scr,image=img)
    l.place(x=0,y=0)
    display=Label(scr,text="Toilet washing".ljust(100),fg="black", bg="aqua",font=("times",20,"bold"))
    display.grid(row=0,column=0)
    v=IntVar()
    opt1=OptionMenu(scr,v,1,2,3,4,5)
    opt1.grid(row=0,column=1)

    display1=Label(scr,text="Toilet floor drying".ljust(98),fg="black",bg="aqua",font=("times",20,"bold"))
    display1.grid(row=1,column=0)
    v1=IntVar()
    opt2=OptionMenu(scr,v1,1,2,3,4,5)
    opt2.grid(row=1,column=1)

    display2=Label(scr,text="Toilet mirror cleaning".ljust(95),fg="black",bg="aqua",font=("times",20,"bold"))
    display2.grid(row=2,column=0)
    v2=IntVar()
    opt3=OptionMenu(scr,v2,1,2,3,4,5)
    opt3.grid(row=2,column=1)

    display3=Label(scr,text="Toilet wash basin cleanng".ljust(92),fg="black",bg="aqua",font=("times",20,"bold"))
    display3.grid(row=3,column=0)
    v3=IntVar()
    opt4=OptionMenu(scr,v3,1,2,3,4,5)
    opt4.grid(row=3,column=1)

    display4=Label(scr,text="Smell of deodorant spray".ljust(91),fg="black",bg="aqua",font=("times",20,"bold"))
    display4.grid(row=4,column=0)
    v4=IntVar()
    opt5=OptionMenu(scr,v4,1,2,3,4,5)
    opt5.grid(row=4,column=1)

    display5=Label(scr,text="Smell of mosquito repellent spray".ljust(86),fg="black",bg="aqua",font=("times",20,"bold"))
    display5.grid(row=5,column=0)
    v5=IntVar()
    opt6=OptionMenu(scr,v5,1,2,3,4,5)
    opt6.grid(row=5,column=1)

    display0=Label(scr,text="Cleaning of coach aisle area with mopper".ljust(80),fg="black",bg="aqua",font=("times",20,"bold"))
    display0.grid(row=6,column=0)
    v6=IntVar()
    opt7=OptionMenu(scr,v6,1,2,3,4,5)
    opt7.grid(row=6,column=1)

    display7=Label(scr,text="Cleaning of door area".ljust(94),fg="black",bg="aqua",font=("times",20,"bold"))
    display7.grid(row=7,column=0)
    v7=IntVar()
    opt8=OptionMenu(scr,v7,1,2,3,4,5)
    opt8.grid(row=7,column=1)

    display8=Label(scr,text="Cleaning of vestibule area".ljust(92),fg="black",bg="aqua",font=("times",20,"bold"))
    display8.grid(row=8,column=0)
    v8=IntVar()
    opt9=OptionMenu(scr,v8,1,2,3,4,5)
    opt9.grid(row=8,column=1)

    display9=Label(scr,text="Cleaning of ac window glasses".ljust(88),fg="black",bg="aqua",font=("times",20,"bold"))
    display9.grid(row=9,column=0)
    v9=IntVar()
    opt10=OptionMenu(scr,v9,1,2,3,4,5)
    opt10.grid(row=9,column=1)

    display10=Label(scr,text="Cleaning of dustbin from ac coach".ljust(85),fg="black",bg="aqua",font=("times",20,"bold"))
    display10.grid(row=10,column=0)
    v10=IntVar()
    opt11=OptionMenu(scr,v10,1,2,3,4,5)
    opt11.grid(row=10,column=1)

    display11=Label(scr,text="Behaviour of worker".ljust(93),fg="black",bg="aqua",font=("times",20,"bold"))
    display11.grid(row=11,column=0)
    v11=IntVar()
    opt12=OptionMenu(scr,v11,1,2,3,4,5)
    opt12.grid(row=11,column=1)

    display12=Label(scr,text="Hygiene and cleanless of worker uniform".ljust(80),fg="black",bg="aqua",font=("times",20,"bold"))
    display12.grid(row=12,column=0)
    v12=IntVar()
    opt13=OptionMenu(scr,v12,1,2,3,4,5)
    opt13.grid(row=12,column=1)


    display13=Label(scr,text="Over all are you satisfied".ljust(94),fg="black",bg="aqua",font=("times",20,"bold"))
    display13.grid(row=13,column=0)
    v13=StringVar()
    opt14=OptionMenu(scr,v13,"Yes","No")
    opt14.grid(row=13,column=1)
    b=Button(scr,text="Submit",command=lambda :addrecord(scr,v.get(),v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get(),v10.get(),v11.get(),v12.get(),v13.get()),fg="black",font=("times",25,"bold"))
    b.grid(row=14,column=1)

def getmypnr(master,pnr_number):
    f1=Frame(master,bg='cyan',width=1200,height=600)
    f1.pack()
    api_key = "yuq0jumj8m" 
    base_url = "https://api.railwayapi.com/v2/pnr-status/pnr/"
    complete_url = base_url + pnr_number + "/apikey/" + api_key + "/"
    response_ob = requests.get(complete_url) 
    result = response_ob.json()  
    if result["response_code"] == 200: 
            train_name = result["train"]["name"] 
            train_number = result["train"]["number"] 
            from_station = result["from_station"]["name"] 
            to_station = result["to_station"]["name"] 
            boarding_point = result["boarding_point"]["name"] 
            reservation_upto = result["reservation_upto"]["name"] 
            pnr_num = result["pnr"] 
            date_of_journey = result["doj"] 
            total_passengers = result["total_passengers"] 
            passengers_list = result["passengers"] 
            chart_prepared = result["chart_prepared"]
            u=Label(f1,text="Train Name",font=("times",10,"bold"))
            u.place(x=10,y=40)
            u1=Label(f1,text="%s"%str(train_name),font=("times",12,"bold"))
            u1.place(x=10,y=60)
            u2=Label(f1,text="Train Number",font=("times",10,"bold"))
            u2.place(x=130,y=40)
            u3=Label(f1,text="%s"%str(train_number),font=("times",12,"bold"))
            u3.place(x=130,y=60)
            u4=Label(f1,text="From Station",font=("times",10,"bold"))
            u4.place(x=250,y=40)
            u5=Label(f1,text="%s"%str(from_station),font=("times",12,"bold"))
            u5.place(x=250,y=60)
            u6=Label(f1,text="To Station",font=("times",10,"bold"))
            u6.place(x=370,y=40)
            u7=Label(f1,text="%s"%str(to_station),font=("times",12,"bold"))
            u7.place(x=370,y=60)
            u8=Label(f1,text="Boarding Point",font=("times",10,"bold"))
            u8.place(x=490,y=40)
            u9=Label(f1,text="%s"%str(boarding_point),font=("times",12,"bold"))
            u9.place(x=490,y=60)
            u10=Label(f1,text="Reservation Upto",font=("times",10,"bold"))
            u10.place(x=610,y=40)
            u11=Label(f1,text="%s"%str(reservation_upto),font=("times",12,"bold"))
            u11.place(x=610,y=60)
            u12=Label(f1,text="Pnr Number",font=("times",10,"bold"))
            u12.place(x=730,y=40)
            u13=Label(f1,text="%s"%str(pnr_num),font=("times",12,"bold"))
            u13.place(x=730,y=60)
            u14=Label(f1,text="Date of Journey",font=("times",10,"underline"))
            u14.place(x=850,y=40)
            u15=Label(f1,text="%s"%str(date_of_journey),font=("times",12,"bold"))
            u15.place(x=850,y=60)
            u16=Label(f1,text="No. Of Passengers",font=("times",10,"bold"))
            u16.place(x=970,y=40)
            u17=Label(f1,text="%s"%str(total_passengers),font=("times",15,"bold"))
            u17.place(x=970,y=60)
            u18=Label(f1,text="chart prepared",font=("times",10,"bold"))
            u18.place(x=1090,y=40)
            u19=Label(f1,text="%s"%str(chart_prepared),font=("times",15,"bold"))
            u19.place(x=1090,y=60)
            # looping through passenger list
            u20=Label(f1,text="passenger number",font=("times",20,"bold"))
            u20.place(x=200,y=100)
            u21=Label(f1,text="current status",font=("times",20,"bold"))
            u21.place(x=500,y=100)
            u22=Label(f1,text="booking_status",font=("times",20,"bold"))
            u22.place(x=900,y=100)
            yx=170
            for passenger in passengers_list:  
                    passenger_num = passenger["no"] 
                    current_status = passenger["current_status"] 
                    booking_status = passenger["booking_status"]
                    u21=Label(f1,text="%s"%str(passenger_num),font=("times",20,"bold"))
                    u21.place(x=200,y=yx)
                    u22=Label(f1,text="%s"%str(current_status),font=("times",20,"bold"))
                    u22.place(x=500,y=yx)
                    u23=Label(f1,text="%s"%str(booking_status),font=("times",20,"bold"))
                    u23.place(x=900,y=yx)
                    yx+=50
    else:
        ueror=Label(f1,text="record is not found for given request",font=("times",20,"bold"))
        ueror.place(x=100,y=40)
    
def Pnrs():
    scr=Tk(className='pnr')
    scr.geometry('1200x800+0+0')
    f=Frame(scr,bg='blue',width=1200,height=200)
    f.pack()
    u=Label(f,text="CHECK PNR STATUS".center(100),bg='cyan',font=("times",20,"underline"),relief='raised')
    u.place(x=200,y=30)
    u1=Label(f,text="Enter PNR(10-DIGITS)",bg='magenta',font=("times",20,"bold"),relief='raised')
    u1.place(x=200,y=80)
    p=Entry(f,bg='magenta',font=("times",20,"underline"),relief='raised')
    p.place(x=500,y=80)
    b=Button(f,text="Get Status",fg='white',relief='raised',bg='gray',font=("times",20,"italic"),command=lambda :getmypnr(scr,p.get()))
    b.place(x=500,y=140)
    scr.mainloop()
    
def PNRST(mag):
    mag.destroy()
    Pnrs()
    myhome()


def admins(mag):
    mag.destroy()
    d=Mygui()
    myhome()
def users(mag):
    mag.destroy()
    home()
    myhome()

def myhome():
    scr=Tk(className='indian railway')
    scr.geometry('1100x700+0+0')
    img=PhotoImage(file="Indian Railway Knowledge Portal.png")
    l=Label(scr,image=img)
    l.place(x=0,y=0)
    l1=Label(scr,text="Welcome to INDIAN RAILWAY NETWORK ",bg='magenta',font=("times",30,"bold"))
    l1.place(x=200,y=30)
    b=Button(scr,text='Admin Pannel'.center(57),font=('times',15,'bold'),bg='blue',relief='raised',bd=10,command=lambda :admins(scr))
    b.place(x=400,y=400)
    b1=Button(scr,text='Passengers FeedBack'.center(50),command=lambda :users(scr),font=('times',15,'bold'),bg='blue',relief='raised',bd=10)
    b1.place(x=400,y=500)
    b2=Button(scr,text='Check PNR Status'.center(53),command=lambda :PNRST(scr),font=('times',15,'bold'),bg='blue',relief='raised',bd=10)
    b2.place(x=400,y=600)
    scr.mainloop()
    
myhome()
