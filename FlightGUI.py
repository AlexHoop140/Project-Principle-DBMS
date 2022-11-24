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

background_img = PhotoImage(file = f"img/background.png")
background = canvas.create_image(
    808.0, 229.0,
    image=background_img)

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

    global plane_id_entry
    global plane_name_entry
    global plane_totalseat_entry
    global plane_seat1_entry
    global plane_seat2_entry
    global plane_manu_entry


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


img0 = PhotoImage(file = f"img/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = plane_management_click,
    relief = "flat")

b0.place(
    x = 828, y = 547,
    width = 338,
    height = 66)

img1 = PhotoImage(file = f"img/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = plane_management_click,
    relief = "flat")

b1.place(
    x = 830, y = 453,
    width = 337,
    height = 69)

img2 = PhotoImage(file = f"img/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = plane_management_click,
    relief = "flat")

b2.place(
    x = 830, y = 363,
    width = 338,
    height = 66)

img3 = PhotoImage(file = f"img/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = plane_management_click,
    relief = "flat")

b3.place(
    x = 828, y = 268,
    width = 338,
    height = 66)

img4 = PhotoImage(file = f"img/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = plane_management_click,
    relief = "flat")

b4.place(
    x = 828, y = 178,
    width = 338,
    height = 66)

window.resizable(False, False)
window.mainloop()