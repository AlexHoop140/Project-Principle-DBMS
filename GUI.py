import main as mn
import mysql.connector
import sys
import random
from tkinter import *

root = Tk()
root.title('DBMS Project')


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
def submit():
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

def show():
    conn = mysql.connector.connect(
        user="root",
        password="FzrTscd0aGODkVIUXtsa",
        host="containers-us-west-44.railway.app",
        port=5960,
        database="railway"
    )
    cur = conn.cursor()

    # Show database
    cur.execute("SELECT * FROM PLANES")
    records = cur.fetchall()

    print_record = ''
    for record in records:
        print_record += str(record) + "\n"

    show_label = Label(root, text=print_record)
    show_label.grid(row=8, column=0, columnspan=2)




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

#Plane insert textbox label
plane_id_label = Label(root,text="Plane ID")
plane_id_label.grid(row=0, column=0)
plane_name_label = Label(root,text="Plane Name")
plane_name_label.grid(row=1, column=0)
plane_total_seat_label = Label(root,text="Total Seat")
plane_total_seat_label.grid(row=2, column=0)
plane_t1_seat_label = Label(root,text="Type 1 seat number")
plane_t1_seat_label.grid(row=3, column=0)
plane_t2_seat_label = Label(root,text="Type 2 seat number")
plane_t2_seat_label.grid(row=4, column=0)
plane_manuf_label = Label(root,text="Manufacturer")
plane_manuf_label.grid(row=5, column=0)

#Plane submit button
p_submit_btn = Button(root, text="Add New Plane To Database", command=submit)
p_submit_btn.grid(row=6,column=0, columnspan=2, padx=10, pady=10,ipadx=100)
p_show_btn = Button(root, text="Show all Planes information", command=show)
p_show_btn.grid(row=7,column=0, columnspan=2, padx=10, pady=10,ipadx=100)

conn.close()

mainloop()