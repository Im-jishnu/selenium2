from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import mysql.connector
# def working_hours():
#     t=Label(window,text="Weekdays timings-10AM to 6PM",font="time gold,16").pack()
def ticket_booking():
    l1 = Label(window, text="NAME",font="time 15 bold")
    l1.place(x=10, y=130)
    e3=Entry(window,font=('arial bold',10,'normal'))
    e3.place(x=100, y=130)
    l2 = Label(window, text="AGE",font="time 15 bold")
    l2.place(x=10, y=170)
    e4=Entry(window,font=('arial bold',10,'normal'))
    e4.place(x=100, y=170)
    c=Label(window,text="GENDER",font="time 15 bold")
    c.place(x=10,y=210)
    var1=StringVar()
    var2=StringVar()
    c1=Checkbutton(window,text="MALE",variable=var1,font="time 10")
    c1.deselect()
    c1.place(x=100,y=210)
    l = Checkbutton(window, text="FEMALE", variable=var2, font="time 10")
    l.deselect()
    l.place(x=180, y=210)
    cal=Calendar(window,setmode="day",date_pattern="d/m/yy")
    cal.place(x=100,y=250)
    opencal=Label(window,text="DATE",font="time 15 bold")
    opencal.place(x=10,y=320)
    l4 = Label(window, text="PH_NO",font="time 15 bold")
    l4.place(x=10, y=490)
    e6 = Entry(window,font=('arial bold',10,'normal'))
    e6.place(x=110, y=490)
    b1 = Button(window, text="BOOK",font="time 15 bold")
    b1.place(x=120, y=550)
window=Tk()
window.title("wonderla amusement park")
label = Label(window, text="WONDERLA AMUSEMENT PARK", font='arial 35 bold',bg="blue")
label.pack()
frame = Frame(window, height=1550, width=1350)
frame.pack()
b2=Button(window,text="SEAT AVAILABILITY",font="time 15 bold",bg="yellow")
b2.place(x=100,y=300)
b3=Button(window,text="WORKING HOURS",font="time 15 bold",bg="yellow")
b3.place(x=400,y=300)
b4=Button(window,text="TICKET BOOKING",font="time 15 bold",bg="yellow",command=ticket_booking).place(x=700, y=300)
b5=Button(window,text="TICKET FARE AND OFFERS",font="time 15 bold",bg="yellow").place(x=1000,y=300)

# window.resizable(False, False)

#ticket booking system
# def ticket_booking():
    # conn=mysql.connector.connect(host="localhost",database="wonderla",user="root",password=1234)
    # cursor=conn.cursor()
#     for user_name,seats in ticket_booking().items():
#         print(f"\n you,{user_name.title()},have chosen{len(seats)}seat(s).")
#         for seat in seats:
#             print(f"\tseat number:{seat}")
# ticket_booking={}
# available_seats=[10]
# if(ticket_booking<=available_seats):
#     messagebox.showinfo("your ticket confirmed")
# else:
#     messagebox.showinfo("no tickets found")


# start_prompt="\n would you like to start booking ticket?(yes/no)"/
# wanted_seats_prompts="\n how many seats are you would like to book:"

# working hours

    # label= Label(window,text="week days : 10.30 AM to 6.00 PM").pack()
    # label = Label(window,text="weekend and public holidays : 10.00 AM to 7.00 PM").pack()









window.mainloop()


