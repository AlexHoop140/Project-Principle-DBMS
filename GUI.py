import main as mn
import mysql.connector
import sys
import random
from tkinter import *

root = Tk()
root.title('DBMS Project')
root.geometry("400x600")


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
                    p_id.get(),
                    p_name.get(),
                    p_total_seat.get(),
                    p_seat1.get(),
                    p_seat2.get(),
                    p_manu.get()
                ))

    conn.commit()
    conn.close()

    #clear current type in content
    p_id.delete(0, END)
    p_name.delete(0, END)
    p_total_seat.delete(0, END)
    p_seat1.delete(0, END)
    p_seat2.delete(0, END)
    p_manu.delete(0, END)

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
    cur.execute("SELECT PLANEID, PLANENAME, TOTALSEAT, TYPE1SEAT,TYPE2SEAT, MANUFACTURER FROM PLANES")
    records = cur.fetchall()

    print_record = ''
    for record in records:
        print_record += str(record) + "\n"

    show_label = Label(root, text=print_record)
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
    cur.execute("DELETE from PLANES WHERE PLANEID=" + "\'" +(p_selected.get()) + "\'")

    p_selected.delete(0, END)

    conn.commit()
    conn.close()

def update():
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
                "WHERE PLANEID=" + "\'" +(p_selected.get()) + "\'",
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
    cur.execute("SELECT * FROM PLANES WHERE PLANEID=" + "\'" +(p_selected.get()) + "\'")
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
    p_save_btn = Button(editor, text="Save", command=update)
    p_save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=145)

    conn.commit()
    conn.close()



#Plane textbox
p_id = Entry(root, width=30)
p_id.grid(row=0, column=1, padx=20)
p_name = Entry(root, width=30)
p_name.grid(row=1, column=1, padx=20)
p_total_seat = Entry(root, width=30)
p_total_seat.grid(row=2, column=1, padx=20)
p_seat1 = Entry(root, width=30)
p_seat1.grid(row=3, column=1, padx=20)
p_seat2 = Entry(root, width=30)
p_seat2.grid(row=4, column=1, padx=20)
p_manu = Entry(root, width=30)
p_manu.grid(row=5, column=1, padx=20)
p_selected = Entry(root, width=30)
p_selected.grid(row=8, column=1, padx=20)

#Plane insert textbox label
plane_id_label = Label(root, text="Plane ID")
plane_id_label.grid(row=0, column=0)
plane_name_label = Label(root, text="Plane Name")
plane_name_label.grid(row=1, column=0)
plane_total_seat_label = Label(root, text="Total Seat")
plane_total_seat_label.grid(row=2, column=0)
plane_t1_seat_label = Label(root, text="Type 1 seat number")
plane_t1_seat_label.grid(row=3, column=0)
plane_t2_seat_label = Label(root, text="Type 2 seat number")
plane_t2_seat_label.grid(row=4, column=0)
plane_manuf_label = Label(root, text="Manufacturer")
plane_manuf_label.grid(row=5, column=0)
plane_selected_label = Label(root, text="Enter Plane ID")
plane_selected_label.grid(row=8, column=0)

# Plane submit button
p_submit_btn = Button(root, text="Add New Plane To Database", command=plane_submit)
p_submit_btn.grid(row=6,column=0, columnspan=2, padx=10, pady=10,ipadx=100)
# Plane show button
p_show_btn = Button(root, text="Show all Planes information", command=plane_show)
p_show_btn.grid(row=7,column=0, columnspan=2, padx=10, pady=10,ipadx=100)

#Plane Delete button
p_delete_btn = Button(root, text="Delete Plane", command=plane_delete)
p_delete_btn.grid(row=9,column=0, columnspan=2, padx=10, pady=10,ipadx=137)

#Plane Update button
p_delete_btn = Button(root, text="Update Plane", command=edit)
p_delete_btn.grid(row=11,column=0, columnspan=2, padx=10, pady=10,ipadx=137)

conn.close()

mainloop()