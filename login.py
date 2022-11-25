from tkinter import *
import tkinter.font as TkFont
from tkinter import messagebox

import mysql.connector
import sys
import re
import passengerdashboard as pdboard
import FlightGUI as empdashboard
import random


def wrong_id_password_popup():
    messagebox.showinfo("Error!", "Sorry, Passenger is not existed!")


def employee_management_ui():
    print("Logged in as employee")


def passenger_management_ui():
    print("Logged in as passenger")


def authenticate(id, password):
    try:
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )

        cur = conn.cursor()
    except mysql.connector.Error as e:
        print(f"Error connecting to Mysql Platform: {e}")
        conn.rollback()
        sys.exit(1)
    if not re.search("[0-9]{10}", password):
        return False
    else:
        if check.get() == 1:
            cur.execute("SELECT * FROM EMPLOYEE WHERE EMPID=%s AND EMPPHONENUM=%s", (id, password,))
            authID = cur.fetchall()
            if len(authID) == 0:
                return False
            else:
                return True
        else:
            cur.execute("SELECT * FROM PASSENGER WHERE PASSID=%s AND PASSPHONENUMBER=%s", (id, password,))
            authID = cur.fetchall()
            if len(authID) == 0:
                return False
            else:
                return True


def btn_clicked():
    inputID = entry0.get()
    inputPassword = entry1.get()

    auth = authenticate(inputID, inputPassword)
    if auth:
        if check.get() == 1:
            empdashboard.employee_management_ui()
        else:
            pdboard.passenger_management_ui(inputID, inputPassword)
    else:
        wrong_id_password_popup()


def var_states():
    if check.get() == 1:
        state = "employee"
        print("Login as employee")
    else:
        state = "passenger"
        print("Login as passenger")


window = Tk()

font = TkFont.Font(family="Helvetica", size=11)

window.geometry("1280x720")
window.configure(bg="#ffffff")
window.title("Log in - Flight Management System")

canvas = Canvas(
    window,
    bg="#ffffff",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"img/login/DBMS-Login-01.png")
background = canvas.create_image(
    640.0, 360.0,
    image=background_img)

entry0_img = PhotoImage(file=f"img/login/img_textBox0.png")
entry0_bg = canvas.create_image(
    201.5, 190.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#B1B2FF",
    font=font,
    highlightthickness=0)

entry0.place(
    x=57, y=168,
    width=289,
    height=43)

img0 = PhotoImage(file=f"img/login/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=372, y=218,
    width=195,
    height=45)

entry1_img = PhotoImage(file=f"img/login/img_textBox1.png")
entry1_bg = canvas.create_image(
    201.5, 285.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    font=font,
    bg="#B1B2FF",
    highlightthickness=0)

entry1.place(
    x=57, y=263,
    width=289,
    height=43)

check = IntVar()

checkbox_img = PhotoImage(file=f"img/login/checkbox-blank-outlineuncheck.png")

checkbox = Checkbutton(window, text="Login as employee", variable=check, command=var_states, font=font, borderwidth=0,
                       background="white", selectimage=checkbox_img)

checkbox.deselect()

checkbox.place(
    x=372, y=170,
    width=195,
    height=35
)

window.resizable(False, False)
window.mainloop()
