from tkinter import *
from PIL import Image, ImageTk
import main as mn
import mysql.connector
import sys
import random


window = Tk()
window.title('Airport Management')
window.geometry("1280x720")
window.configure(bg = "#171717")
canvas = Canvas(
    window,
    bg = "#171717",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)



############### CONNECTION SECTION ################
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

#Plane submit function
def plane_submit():
    #create database connection
    conn = mysql.connector.connect(
        user="root",
        password="FzrTscd0aGODkVIUXtsa",
        host="containers-us-west-44.railway.app",
        port=5960,
        database="railway"
    )
    cur = conn.cursor()

    # Insert into table
    cur.execute("INSERT INTO PLANES VALUES(%s, %s, %s, %s, %s, %s)",
                (
                    plane_id_entry.get(),
                    plane_name_entry.get(),
                    plane_totalseat_entry.get(),
                    plane_seat1_entry.get(),
                    plane_seat1_entry.get(),
                    plane_manu_entry.get()
                ))

    conn.commit()
    conn.close()

    #clear current type in content
    plane_id_entry.delete(0, END)
    plane_name_entry.delete(0, END)
    plane_totalseat_entry.delete(0, END)
    plane_seat1_entry.delete(0, END)
    plane_seat1_entry.delete(0, END)
    plane_manu_entry.delete(0, END)

def plane_show():
    conn = mysql.connector.connect(
        user="root",
        password="FzrTscd0aGODkVIUXtsa",
        host="containers-us-west-44.railway.app",
        port=5960,
        database="railway"
    )
    cur = conn.cursor()

    # Show database
    plane_show = Toplevel(window)
    cur.execute("SELECT PLANEID, PLANENAME, TOTALSEAT, TYPE1SEAT,TYPE2SEAT, MANUFACTURER FROM PLANES")
    records = cur.fetchall()

    print_record = ''
    for record in records:
        print_record += str(record) + "\n"

    show_label = Label(plane_show, text=print_record)
    show_label.grid(row=10, column=0, columnspan=2)

    conn.commit()
    conn.close()

def plane_delete():
    conn = mysql.connector.connect(
        user="root",
        password="FzrTscd0aGODkVIUXtsa",
        host="containers-us-west-44.railway.app",
        port=5960,
        database="railway"
    )
    cur = conn.cursor()

    #delete
    cur.execute("DELETE from PLANES WHERE PLANEID=" + "\'" +(plane_edit_entry.get()) + "\'")

    plane_edit_entry.delete(0, END)

    conn.commit()
    conn.close()

def plane_update():
    conn = mysql.connector.connect(
        user="root",
        password="FzrTscd0aGODkVIUXtsa",
        host="containers-us-west-44.railway.app",
        port=5960,
        database="railway"
    )
    cur = conn.cursor()

    cur.execute("UPDATE PLANES SET "
                "PLANEID = %s, "
                "PLANENAME = %s, "
                "TOTALSEAT = %s, "
                "TYPE1SEAT = %s, "
                "TYPE2SEAT = %s,"
                "MANUFACTURER = %s "
                "WHERE PLANEID=" + "\'" +(plane_edit_entry.get()) + "\'",
                (
                    p_id_editor.get(),
                    p_name_editor.get(),
                    p_total_seat_editor.get(),
                    p_seat1_editor.get(),
                    p_seat2_editor.get(),
                    p_manu_editor.get()
                ))

    conn.commit()
    conn.close()
    editor.destroy()
def edit():
    global editor
    editor = Tk()
    editor.title('Update Plane')
    editor.geometry("400x300")

    conn = mysql.connector.connect(
        user="root",
        password="FzrTscd0aGODkVIUXtsa",
        host="containers-us-west-44.railway.app",
        port=5960,
        database="railway"
    )
    cur = conn.cursor()

    #Edit plane
    cur.execute("SELECT * FROM PLANES WHERE PLANEID=" + "\'" +(plane_edit_entry.get()) + "\'")
    records = cur.fetchall()

    #define global var
    global p_id_editor
    global p_name_editor
    global p_total_seat_editor
    global p_seat1_editor
    global p_seat2_editor
    global p_manu_editor

    # Plane textbox
    p_id_editor = Entry(editor, width=30)
    p_id_editor.grid(row=0, column=1, padx=20)
    p_name_editor = Entry(editor, width=30)
    p_name_editor.grid(row=1, column=1, padx=20)
    p_total_seat_editor = Entry(editor, width=30)
    p_total_seat_editor.grid(row=2, column=1, padx=20)
    p_seat1_editor = Entry(editor, width=30)
    p_seat1_editor.grid(row=3, column=1, padx=20)
    p_seat2_editor = Entry(editor, width=30)
    p_seat2_editor.grid(row=4, column=1, padx=20)
    p_manu_editor = Entry(editor, width=30)
    p_manu_editor.grid(row=5, column=1, padx=20)

    # Plane insert textbox label
    plane_id_label_editor = Label(editor, text="Plane ID")
    plane_id_label_editor.grid(row=0, column=0)
    plane_name_label_editor = Label(editor, text="Plane Name")
    plane_name_label_editor.grid(row=1, column=0)
    plane_total_seat_label_editor = Label(editor, text="Total Seat")
    plane_total_seat_label_editor.grid(row=2, column=0)
    plane_t1_seat_label_editor = Label(editor, text="Type 1 seat number")
    plane_t1_seat_label_editor.grid(row=3, column=0)
    plane_t2_seat_label_editor = Label(editor, text="Type 2 seat number")
    plane_t2_seat_label_editor.grid(row=4, column=0)
    plane_manuf_label_editor = Label(editor, text="Manufacturer")
    plane_manuf_label_editor.grid(row=5, column=0)

    #Insert default value
    for record in records:
        p_id_editor.insert(0, record[0])
        p_name_editor.insert(0, record[1])
        p_total_seat_editor.insert(0, record[2])
        p_seat1_editor.insert(0, record[3])
        p_seat2_editor.insert(0, record[4])
        p_manu_editor.insert(0, record[5])

    # Plane update Save button
    p_save_btn = Button(editor, text="Save", command=plane_update)
    p_save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=145)

    conn.commit()
    conn.close()

background_img = PhotoImage(file = f"img/AirportManagement/background.png")
background = canvas.create_image(
    808.0, 229.0,
    image=background_img)

def btn_clicked():
    print("Button Clicked")

def plane_management_click():
    plane_window = Toplevel(window)

    plane_window.geometry("600x900")
    plane_window.configure(bg="#9ba4b4")
    plane_window.title('Plane Management')
    plane_canvas = Canvas(
        plane_window,
        bg="#9ba4b4",
        height=900,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    plane_canvas.place(x=0, y=0)
    global plane_background_img

    plane_background_img = PhotoImage(file=f"img/Plane/background.png")
    plane_canvas.create_image(
        165.0, 423.5,
        image=plane_background_img)

    global plane_id_entry_img
    global plane_name_entry_img
    global plane_totalseat_entry_img
    global plane_seat1_entry_img
    global plane_seat2_entry_img
    global plane_manu_entry_img


    plane_id_entry_img = PhotoImage(file=f"img/Plane/img_textBox0.png")
    plane_id_entry_bg = plane_canvas.create_image(
        290.0, 91.5,
        image=plane_id_entry_img)

    plane_id_entry = Entry(
        plane_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    plane_id_entry.place(
        x=82, y=73,
        width=416,
        height=35)

    plane_name_entry_img = PhotoImage(file=f"img/Plane/img_textBox1.png")
    plane_name_entry_bg = plane_canvas.create_image(
        290.0, 169.5,
        image=plane_name_entry_img)

    plane_name_entry = Entry(
        plane_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    plane_name_entry.place(
        x=82, y=151,
        width=416,
        height=35)

    plane_totalseat_entry_img = PhotoImage(file=f"img/Plane/img_textBox2.png")
    plane_totalseat_entry_bg = plane_canvas.create_image(
        291.0, 246.5,
        image=plane_totalseat_entry_img)

    plane_totalseat_entry = Entry(
        plane_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    plane_totalseat_entry.place(
        x=83, y=228,
        width=416,
        height=35)

    plane_seat1_entry_img = PhotoImage(file=f"img/Plane/img_textBox3.png")
    plane_seat1_entry_bg = plane_canvas.create_image(
        176.5, 323.5,
        image=plane_seat1_entry_img)

    plane_seat1_entry = Entry(
        plane_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    plane_seat1_entry.place(
        x=83, y=305,
        width=187,
        height=35)

    plane_seat1_entry_img = PhotoImage(file=f"img/Plane/img_textBox4.png")
    plane_seat1_entry_bg = plane_canvas.create_image(
        405.5, 323.5,
        image=plane_seat1_entry_img)

    plane_seat1_entry = Entry(
        plane_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    plane_seat1_entry.place(
        x=312, y=305,
        width=187,
        height=35)

    plane_manu_entry_img = PhotoImage(file=f"img/Plane/img_textBox5.png")
    plane_manu_entry_bg = plane_canvas.create_image(
        290.0, 401.5,
        image=plane_manu_entry_img)

    plane_manu_entry = Entry(
        plane_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    plane_manu_entry.place(
        x=82, y=383,
        width=416,
        height=35)


    global plane_img0
    plane_img0 = PhotoImage(file=f"img/Plane/img0.png")
    plane_b0 = Button(
        plane_window,
        image=plane_img0,
        borderwidth=0,
        highlightthickness=0,
        command=plane_submit,
        relief="flat")

    plane_b0.place(
        x=144, y=452,
        width=293,
        height=62)


    global plane_img1
    plane_img1 = PhotoImage(file=f"img/Plane/img1.png")
    plane_b1 = Button(
        plane_window,
        image=plane_img1,
        borderwidth=0,
        highlightthickness=0,
        command=plane_show,
        relief="flat")

    plane_b1.place(
        x=144, y=530,
        width=293,
        height=62)

    global plane_edit_entry
    plane_edit_entry_img = PhotoImage(file=f"img/Plane/img_textBox6.png")
    plane_edit_entry_bg = plane_canvas.create_image(
        290.0, 674.5,
        image=plane_edit_entry_img)

    plane_edit_entry = Entry(
        plane_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    plane_edit_entry.place(
        x=82, y=656,
        width=416,
        height=35)

    global plane_img2
    plane_img2 = PhotoImage(file=f"img/Plane/img2.png")
    plane_b2 = Button(
        plane_window,
        image=plane_img2,
        borderwidth=0,
        highlightthickness=0,
        command=edit,
        relief="flat")

    plane_b2.place(
        x = 83, y = 741,
        width=187,
        height=62)

    global plane_img3
    plane_img3 = PhotoImage(file=f"img/Plane/img3.png")
    plane_b3 = Button(
        plane_window,
        image=plane_img3,
        borderwidth=0,
        highlightthickness=0,
        command=plane_delete,
        relief="flat")

    plane_b3.place(
        x=308, y=741,
        width=187,
        height=62)

def flight_management_click():
    flight_window = Toplevel(window)

    flight_window.geometry("600x900")
    flight_window.configure(bg="#9ba4b4")
    flight_window.title('Flight Management')
    canvas = Canvas(
        flight_window,
        bg="#9ba4b4",
        height=900,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    # set global all img
    global flight_background_img
    global flight_entry0_img
    global flight_entry1_img
    global flight_entry2_img
    global flight_entry3_img
    global flight_entry4_img
    global flight_entry5_img
    global flight_entry6_img
    global flight_entry7_img
    global flight_entry8_img
    global flight_entry9_img
    global flight_img0
    global flight_img1
    global flight_img2
    global flight_img3

    flight_background_img = PhotoImage(file=f"img/Flight/background.png")
    flight_background = canvas.create_image(
        300.0, 473.0,
        image=flight_background_img)

    flight_entry0_img = PhotoImage(file=f"img/Flight/img_textBox0.png")
    flight_entry0_bg = canvas.create_image(
        289.0, 99.5,
        image=flight_entry0_img)

    flight_entry0 = Entry(
        flight_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    flight_entry0.place(
        x=81, y=81,
        width=416,
        height=35)

    flight_entry1_img = PhotoImage(file=f"img/Flight/img_textBox1.png")
    flight_entry1_bg = canvas.create_image(
        289.0, 177.5,
        image=flight_entry1_img)

    flight_entry1 = Entry(
        flight_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    flight_entry1.place(
        x=81, y=159,
        width=416,
        height=35)

    flight_entry2_img = PhotoImage(file=f"img/Flight/img_textBox2.png")
    flight_entry2_bg = canvas.create_image(
        175.5, 254.5,
        image=flight_entry2_img)

    flight_entry2 = Entry(
        flight_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    flight_entry2.place(
        x=82, y=236,
        width=187,
        height=35)

    flight_entry3_img = PhotoImage(file=f"img/Flight/img_textBox3.png")
    flight_entry3_bg = canvas.create_image(
        404.5, 254.5,
        image=flight_entry3_img)

    flight_entry3 = Entry(
        flight_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    flight_entry3.place(
        x=311, y=236,
        width=187,
        height=35)

    flight_entry4_img = PhotoImage(file=f"img/Flight/img_textBox4.png")
    flight_entry4_bg = canvas.create_image(
        175.5, 331.5,
        image=flight_entry4_img)

    flight_entry4 = Entry(
        flight_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    flight_entry4.place(
        x=82, y=313,
        width=187,
        height=35)

    flight_entry5_img = PhotoImage(file=f"img/Flight/img_textBox5.png")
    flight_entry5_bg = canvas.create_image(
        404.5, 331.5,
        image=flight_entry5_img)

    flight_entry5 = Entry(
        flight_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    flight_entry5.place(
        x=311, y=313,
        width=187,
        height=35)

    flight_entry6_img = PhotoImage(file=f"img/Flight/img_textBox6.png")
    flight_entry6_bg = canvas.create_image(
        175.5, 407.5,
        image=flight_entry6_img)

    flight_entry6 = Entry(
        flight_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    flight_entry6.place(
        x=82, y=389,
        width=187,
        height=35)

    flight_entry7_img = PhotoImage(file=f"img/Flight/img_textBox7.png")
    flight_entry7_bg = canvas.create_image(
        404.5, 407.5,
        image=flight_entry7_img)

    flight_entry7 = Entry(
        flight_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    flight_entry7.place(
        x=311, y=389,
        width=187,
        height=35)

    flight_entry8_img = PhotoImage(file=f"img/Flight/img_textBox8.png")
    flight_entry8_bg = canvas.create_image(
        288.0, 483.5,
        image=flight_entry8_img)

    flight_entry8 = Entry(
        flight_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    flight_entry8.place(
        x=80, y=465,
        width=416,
        height=35)

    flight_img0 = PhotoImage(file=f"img/Flight/img0.png")
    flight_b0 = Button(
        flight_window,
        image=flight_img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    flight_b0.place(
        x=83, y=530,
        width=187,
        height=62)

    flight_img1 = PhotoImage(file=f"img/Flight/img1.png")
    flight_b1 = Button(
        flight_window,
        image=flight_img1,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    flight_b1.place(
        x=306, y=530,
        width=187,
        height=62)

    flight_entry9_img = PhotoImage(file=f"img/Flight/img_textBox9.png")
    flight_entry9_bg = canvas.create_image(
        290.0, 674.5,
        image=flight_entry9_img)

    flight_entry9 = Entry(
        flight_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    flight_entry9.place(
        x=82, y=656,
        width=416,
        height=35)

    flight_img2 = PhotoImage(file=f"img/Flight/img2.png")
    flight_b2 = Button(
        flight_window,
        image=flight_img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    flight_b2.place(
        x=83, y=741,
        width=187,
        height=62)

    flight_img3 = PhotoImage(file=f"img/Flight/img3.png")
    flight_b3 = Button(
        flight_window,
        image=flight_img3,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    flight_b3.place(
        x=308, y=741,
        width=187,
        height=62)

def employee_management_click():
    employee_window = Toplevel(window)

    employee_window.geometry("600x900")
    employee_window.configure(bg="#000000")
    employee_window.title('Employee Management')
    canvas = Canvas(
        employee_window,
        bg="#000000",
        height=900,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    # set global all img
    global employee_background_img
    global employee_entry0_img
    global employee_entry1_img
    global employee_entry2_img
    global employee_entry3_img
    global employee_entry4_img
    global employee_entry5_img
    global employee_img0
    global employee_img1
    global employee_img2
    global employee_img3

    employee_background_img = PhotoImage(file=f"img/Employee/background.png")
    employee_background = canvas.create_image(
        300.0, 434.0,
        image=employee_background_img)

    employee_entry0_img = PhotoImage(file=f"img/Employee/img_textBox0.png")
    employee_entry0_bg = canvas.create_image(
        289.0, 99.5,
        image=employee_entry0_img)

    employee_entry0 = Entry(
        employee_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    employee_entry0.place(
        x=81, y=81,
        width=416,
        height=35)

    employee_entry1_img = PhotoImage(file=f"img/Employee/img_textBox1.png")
    employee_entry1_bg = canvas.create_image(
        289.0, 177.5,
        image=employee_entry1_img)

    employee_entry1 = Entry(
        employee_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    employee_entry1.place(
        x=81, y=159,
        width=416,
        height=35)

    employee_entry2_img = PhotoImage(file=f"img/Employee/img_textBox2.png")
    employee_entry2_bg = canvas.create_image(
        287.0, 260.5,
        image=employee_entry2_img)

    employee_entry2 = Entry(
        employee_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    employee_entry2.place(
        x=79, y=242,
        width=416,
        height=35)

    employee_entry3_img = PhotoImage(file=f"img/Employee/img_textBox3.png")
    employee_entry3_bg = canvas.create_image(
        287.0, 338.5,
        image=employee_entry3_img)

    employee_entry3 = Entry(
        employee_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    employee_entry3.place(
        x=79, y=320,
        width=416,
        height=35)

    employee_entry4_img = PhotoImage(file=f"img/Employee/img_textBox4.png")
    employee_entry4_bg = canvas.create_image(
        287.0, 415.5,
        image=employee_entry4_img)

    employee_entry4 = Entry(
        employee_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    employee_entry4.place(
        x=79, y=397,
        width=416,
        height=35)

    employee_img0 = PhotoImage(file=f"img/Employee/img0.png")
    employee_b0 = Button(
        employee_window,
        image=employee_img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    employee_b0.place(
        x=195, y=474,
        width=187,
        height=62)

    employee_img1 = PhotoImage(file=f"img/Employee/img1.png")
    employee_b1 = Button(
        employee_window,
        image=employee_img1,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    employee_b1.place(
        x=195, y=546,
        width=187,
        height=62)

    employee_entry5_img = PhotoImage(file=f"img/Employee/img_textBox5.png")
    employee_entry5_bg = canvas.create_image(
        290.0, 674.5,
        image=employee_entry5_img)

    employee_entry5 = Entry(
        employee_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    employee_entry5.place(
        x=82, y=656,
        width=416,
        height=35)

    employee_img2 = PhotoImage(file=f"img/Employee/img2.png")
    employee_b2 = Button(
        employee_window,
        image=employee_img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    employee_b2.place(
        x=83, y=741,
        width=187,
        height=62)

    employee_img3 = PhotoImage(file=f"img/Employee/img3.png")
    employee_b3 = Button(
        employee_window,
        image=employee_img3,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    employee_b3.place(
        x=308, y=741,
        width=187,
        height=62)

def passenger_management_click():
    passenger_window = Toplevel(window)

    passenger_window.geometry("600x900")
    passenger_window.configure(bg="#000000")
    passenger_window.title('Passenger Management')
    canvas = Canvas(
        passenger_window,
        bg="#000000",
        height=900,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    # global all img
    global passenger_background_img
    global passenger_entry0_img
    global passenger_entry1_img
    global passenger_entry2_img
    global passenger_entry3_img
    global passenger_entry4_img
    global passenger_entry5_img
    global passenger_img0
    global passenger_img1
    global passenger_img2
    global passenger_img3

    passenger_background_img = PhotoImage(file=f"img/Passenger/background.png")
    passenger_background = canvas.create_image(
        300.0, 401.0,
        image=passenger_background_img)

    passenger_entry0_img = PhotoImage(file=f"img/Passenger/img_textBox0.png")
    passenger_entry0_bg = canvas.create_image(
        289.0, 99.5,
        image=passenger_entry0_img)

    passenger_entry0 = Entry(
        passenger_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    passenger_entry0.place(
        x=81, y=81,
        width=416,
        height=35)

    passenger_entry1_img = PhotoImage(file=f"img/Passenger/img_textBox1.png")
    passenger_entry1_bg = canvas.create_image(
        289.0, 177.5,
        image=passenger_entry1_img)

    passenger_entry1 = Entry(
        passenger_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    passenger_entry1.place(
        x=81, y=159,
        width=416,
        height=35)

    passenger_entry2_img = PhotoImage(file=f"img/Passenger/img_textBox2.png")
    passenger_entry2_bg = canvas.create_image(
        287.0, 260.5,
        image=passenger_entry2_img)

    passenger_entry2 = Entry(
        passenger_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    passenger_entry2.place(
        x=79, y=242,
        width=416,
        height=35)

    passenger_entry3_img = PhotoImage(file=f"img/Passenger/img_textBox3.png")
    passenger_entry3_bg = canvas.create_image(
        287.0, 338.5,
        image=passenger_entry3_img)

    passenger_entry3 = Entry(
        passenger_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    passenger_entry3.place(
        x=79, y=320,
        width=416,
        height=35)

    passenger_entry4_img = PhotoImage(file=f"img/Passenger/img_textBox4.png")
    passenger_entry4_bg = canvas.create_image(
        287.0, 415.5,
        image=passenger_entry4_img)

    passenger_entry4 = Entry(
        passenger_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    passenger_entry4.place(
        x=79, y=397,
        width=416,
        height=35)

    passenger_img0 = PhotoImage(file=f"img/Passenger/img0.png")
    passenger_b0 = Button(
        passenger_window,
        image=passenger_img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    passenger_b0.place(
        x=195, y=474,
        width=187,
        height=62)

    passenger_img1 = PhotoImage(file=f"img/Passenger/img1.png")
    passenger_b1 = Button(
        passenger_window,
        image=passenger_img1,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    passenger_b1.place(
        x=195, y=546,
        width=187,
        height=62)

    passenger_entry5_img = PhotoImage(file=f"img/Passenger/img_textBox5.png")
    passenger_entry5_bg = canvas.create_image(
        290.0, 674.5,
        image=passenger_entry5_img)

    passenger_entry5 = Entry(
        passenger_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    passenger_entry5.place(
        x=82, y=656,
        width=416,
        height=35)

    passenger_img2 = PhotoImage(file=f"img/Passenger/img2.png")
    passenger_b2 = Button(
        passenger_window,
        image=passenger_img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    passenger_b2.place(
        x=83, y=741,
        width=187,
        height=62)

    passenger_img3 = PhotoImage(file=f"img/Passenger/img3.png")
    b3 = Button(
        passenger_window,
        image=passenger_img3,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b3.place(
        x=308, y=741,
        width=187,
        height=62)

img0 = PhotoImage(file = f"img/AirportManagement/img0.png")
passenger_button = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = passenger_management_click,
    relief = "flat")

passenger_button.place(
    x = 828, y = 547,
    width = 338,
    height = 66)

img1 = PhotoImage(file = f"img/AirportManagement/img1.png")
employee_button = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = employee_management_click,
    relief = "flat")

employee_button.place(
    x = 830, y = 453,
    width = 337,
    height = 69)

img2 = PhotoImage(file = f"img/AirportManagement/img2.png")
ticket_button = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = plane_management_click,
    relief = "flat")

ticket_button.place(
    x = 830, y = 363,
    width = 338,
    height = 66)

img3 = PhotoImage(file = f"img/AirportManagement/img3.png")
flight_button = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = flight_management_click,
    relief = "flat")

flight_button.place(
    x = 828, y = 268,
    width = 338,
    height = 66)

img4 = PhotoImage(file = f"img/AirportManagement/img4.png")
plane_button = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = plane_management_click,
    relief = "flat")

plane_button.place(
    x = 828, y = 178,
    width = 338,
    height = 66)

window.resizable(False, False)
window.mainloop()