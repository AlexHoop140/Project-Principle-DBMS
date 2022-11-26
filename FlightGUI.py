from tkinter import *
from tkinter import ttk
import mysql.connector
import sys


def employee_management_ui():
    window = Toplevel()
    window.title('Airport Management')
    window.geometry("1280x720")
    window.configure(bg="#171717")
    canvas = Canvas(
        window,
        bg="#171717",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    global background_img
    global img0
    global img1
    global img2
    global img3
    global img4

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

    # Plane submit function
    def plane_submit():
        # create database connection
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
                        plane_seat2_entry.get(),
                        plane_manu_entry.get()
                    ))

        conn.commit()
        conn.close()

        # clear current type in content
        plane_id_entry.delete(0, END)
        plane_name_entry.delete(0, END)
        plane_totalseat_entry.delete(0, END)
        plane_seat1_entry.delete(0, END)
        plane_seat2_entry.delete(0, END)
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
        cur.execute("SELECT PLANEID, PLANENAME, TOTALSEAT, TYPE1SEAT,TYPE2SEAT, MANUFACTURER FROM PLANES")
        planes = cur.fetchall()

        # print_record = ''
        # for record in records:
        #     print_record += str(record) + "\n"

        # show_label = Label(plane_show, text=print_record)
        # show_label.grid(row=10, column=0, columnspan=2)

        available_planes_window = Toplevel()
        available_planes_window.title("All planes information")

        all_planes_table_view = ttk.Treeview(available_planes_window)

        # User Interface Section
        # Define column
        all_planes_table_view['columns'] = ("Plane ID", "Plane Name", "Total Seat",
                                            "Number of seat 1", "Number of seat 2", "Manufacturer")

        # Format columns
        all_planes_table_view.column("#0", width=0, stretch=NO)
        all_planes_table_view.column("Plane ID", anchor=W, width=80)
        all_planes_table_view.column("Plane Name", anchor=W, width=80)
        all_planes_table_view.column("Total Seat", anchor=E, width=80)
        all_planes_table_view.column("Number of seat 1", anchor=E, width=80)
        all_planes_table_view.column("Number of seat 2", anchor=E, width=80)
        all_planes_table_view.column("Manufacturer", anchor=W, width=120)

        # Create heading
        all_planes_table_view.heading("#0", text="", anchor=W)
        all_planes_table_view.heading("Plane ID", text="Plane ID", anchor=CENTER)
        all_planes_table_view.heading("Plane Name", text="Plane Name", anchor=CENTER)
        all_planes_table_view.heading("Total Seat", text="Total Seat", anchor=CENTER)
        all_planes_table_view.heading("Number of seat 1", text="Available seat type 1", anchor=CENTER)
        all_planes_table_view.heading("Number of seat 2", text="Available seat type 2", anchor=CENTER)
        all_planes_table_view.heading("Manufacturer", text="Manufacturer", anchor=CENTER)

        count = 0
        for plane in planes:
            all_planes_table_view.insert(parent='', index='end', iid=str(count), text="", values=(str(plane[0]),
                                                                                                  str(plane[1]),
                                                                                                  str(plane[2]),
                                                                                                  str(plane[3]),
                                                                                                  str(plane[4]),
                                                                                                  str(plane[5])))
            count += 1

        all_planes_table_view.pack(padx=20, pady=20)

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

        # delete
        cur.execute("DELETE from PLANES WHERE PLANEID=" + "\'" + (plane_edit_entry.get()) + "\'")

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
                    "WHERE PLANEID=" + "\'" + (plane_edit_entry.get()) + "\'",
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

    def plane_edit():
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

        # Edit plane
        cur.execute("SELECT * FROM PLANES WHERE PLANEID=" + "\'" + (plane_edit_entry.get()) + "\'")
        records = cur.fetchall()

        # define global var
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

        # Insert default value
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

    # Flight function to Add Show Delete & Update
    def flight_submit():
        # create database connection
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # Insert into table
        cur.execute("INSERT INTO FLIGHT VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        flight_entry0.get(),
                        flight_entry1.get(),
                        flight_entry2.get(),
                        flight_entry3.get(),
                        flight_entry4.get(),
                        flight_entry5.get(),
                        flight_entry6.get(),
                        flight_entry7.get(),
                        flight_entry8.get()
                    ))

        conn.commit()
        conn.close()

        # clear current type in content
        flight_entry0.delete(0, END)
        flight_entry1.delete(0, END)
        flight_entry2.delete(0, END)
        flight_entry3.delete(0, END)
        flight_entry4.delete(0, END)
        flight_entry5.delete(0, END)
        flight_entry6.delete(0, END)
        flight_entry7.delete(0, END)
        flight_entry8.delete(0, END)

    def flight_show():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # Show database
        cur.execute("SELECT * FROM FLIGHT")
        flights = cur.fetchall()

        # print_record = ''
        # for record in records:
        #     print_record += str(record) + "\n"
        #
        # show_label = Label(flight_show, text=print_record)
        # show_label.grid(row=10, column=0, columnspan=2)

        available_flights_window = Toplevel()
        available_flights_window.title("All flights information")

        all_flight_table_view = ttk.Treeview(available_flights_window)

        # User Interface Section
        # Define column
        all_flight_table_view['columns'] = ("Flight ID", "Plane ID", "Departure Date", "Arrival Date", "Origin",
                                            "Destination", "Number of seat 1", "Number of seat 2")

        # Format columns
        all_flight_table_view.column("#0", width=0, stretch=NO)
        all_flight_table_view.column("Flight ID", anchor=W, width=80)
        all_flight_table_view.column("Plane ID", anchor=W, width=80)
        all_flight_table_view.column("Departure Date", anchor=CENTER, width=100)
        all_flight_table_view.column("Arrival Date", anchor=CENTER, width=80)
        all_flight_table_view.column("Origin", anchor=CENTER, width=80)
        all_flight_table_view.column("Destination", anchor=CENTER, width=80)
        all_flight_table_view.column("Number of seat 1", anchor=E, width=120)
        all_flight_table_view.column("Number of seat 2", anchor=E, width=120)

        # Create heading
        all_flight_table_view.heading("#0", text="", anchor=W)
        all_flight_table_view.heading("Flight ID", text="Flight ID", anchor=CENTER)
        all_flight_table_view.heading("Plane ID", text="Plane ID", anchor=CENTER)
        all_flight_table_view.heading("Departure Date", text="Departure Date", anchor=CENTER)
        all_flight_table_view.heading("Arrival Date", text="Arrival Date", anchor=CENTER)
        all_flight_table_view.heading("Origin", text="Origin", anchor=CENTER)
        all_flight_table_view.heading("Destination", text="Destination", anchor=CENTER)
        all_flight_table_view.heading("Number of seat 1", text="Available seat type 1", anchor=CENTER)
        all_flight_table_view.heading("Number of seat 2", text="Available seat type 2", anchor=CENTER)

        count = 0
        for flight in flights:
            all_flight_table_view.insert(parent='', index='end', iid=str(count), text="", values=(str(flight[0]),
                                                                                                  str(flight[1]),
                                                                                                  str(flight[2]),
                                                                                                  str(flight[3]),
                                                                                                  str(flight[5]),
                                                                                                  str(flight[4]),
                                                                                                  str(flight[6]),
                                                                                                  str(flight[7]),))
            count += 1

        all_flight_table_view.pack(padx=20, pady=20)

        conn.commit()
        conn.close()

    def flight_delete():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # delete
        cur.execute("DELETE FROM FLIGHT WHERE FLIGHTID=" + "\'" + (flight_entry9.get()) + "\'")

        flight_entry9.delete(0, END)

        conn.commit()
        conn.close()

    def flight_update():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        cur.execute("UPDATE FLIGHT SET "
                    "FLIGHTID = %s, "
                    "PLANEID = %s, "
                    "DEPARTURE_DATE = %s, "
                    "ARRIVAL_DATE = %s, "
                    "DESTINATION = %s, "
                    "ORIGIN = %s, "
                    "QUANTITY_SEAT1 = %s, "
                    "QUANTITY_SEAT2 = %s, "
                    "NOTE = %s "
                    "WHERE FLIGHTID=" + "\'" + (f_entry0_editor.get()) + "\'",
                    (
                        f_entry0_editor.get(),
                        f_entry1_editor.get(),
                        f_entry2_editor.get(),
                        f_entry3_editor.get(),
                        f_entry4_editor.get(),
                        f_entry5_editor.get(),
                        f_entry6_editor.get(),
                        f_entry7_editor.get(),
                        f_entry8_editor.get()
                    ))

        conn.commit()
        conn.close()
        flight_editor.destroy()

    def flight_edit():
        global flight_editor
        flight_editor = Toplevel(window)
        flight_editor.title('Update Plane')
        flight_editor.geometry("400x300")

        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # Edit plane
        cur.execute("SELECT * FROM FLIGHT WHERE FLIGHTID=" + "\'" + (flight_entry9.get()) + "\'")
        flight_records = cur.fetchall()

        # define global var
        global f_entry0_editor
        global f_entry1_editor
        global f_entry2_editor
        global f_entry3_editor
        global f_entry4_editor
        global f_entry5_editor
        global f_entry6_editor
        global f_entry7_editor
        global f_entry8_editor

        # Plane textbox
        f_entry0_editor = Entry(flight_editor, width=30)
        f_entry0_editor.grid(row=0, column=1, padx=20)
        f_entry1_editor = Entry(flight_editor, width=30)
        f_entry1_editor.grid(row=1, column=1, padx=20)
        f_entry2_editor = Entry(flight_editor, width=30)
        f_entry2_editor.grid(row=2, column=1, padx=20)
        f_entry3_editor = Entry(flight_editor, width=30)
        f_entry3_editor.grid(row=3, column=1, padx=20)
        f_entry4_editor = Entry(flight_editor, width=30)
        f_entry4_editor.grid(row=4, column=1, padx=20)
        f_entry5_editor = Entry(flight_editor, width=30)
        f_entry5_editor.grid(row=5, column=1, padx=20)
        f_entry6_editor = Entry(flight_editor, width=30)
        f_entry6_editor.grid(row=6, column=1, padx=20)
        f_entry7_editor = Entry(flight_editor, width=30)
        f_entry7_editor.grid(row=7, column=1, padx=20)
        f_entry8_editor = Entry(flight_editor, width=30)
        f_entry8_editor.grid(row=8, column=1, padx=20)

        # Plane insert textbox label
        f_label0_editor = Label(flight_editor, text="Flight ID")
        f_label0_editor.grid(row=0, column=0)
        f_label1_editor = Label(flight_editor, text="Plane Plane")
        f_label1_editor.grid(row=1, column=0)
        f_label2_editor = Label(flight_editor, text="Departure Date")
        f_label2_editor.grid(row=2, column=0)
        f_label3_editor = Label(flight_editor, text="Landing Date")
        f_label3_editor.grid(row=3, column=0)
        f_label4_editor = Label(flight_editor, text="Destination")
        f_label4_editor.grid(row=4, column=0)
        f_label5_editor = Label(flight_editor, text="Origin")
        f_label5_editor.grid(row=5, column=0)
        f_label6_editor = Label(flight_editor, text="Number of s1")
        f_label6_editor.grid(row=6, column=0)
        f_label7_editor = Label(flight_editor, text="Number of s2")
        f_label7_editor.grid(row=7, column=0)
        f_label8_editor = Label(flight_editor, text="Note")
        f_label8_editor.grid(row=8, column=0)

        # Insert default value
        for record in flight_records:
            f_entry0_editor.insert(0, record[0])
            f_entry1_editor.insert(0, record[1])
            f_entry2_editor.insert(0, record[2])
            f_entry3_editor.insert(0, record[3])
            f_entry4_editor.insert(0, record[4])
            f_entry5_editor.insert(0, record[5])
            f_entry6_editor.insert(0, record[6])
            f_entry7_editor.insert(0, record[7])
            f_entry8_editor.insert(0, record[8])

        # Plane update Save button
        f_save_btn = Button(flight_editor, text="Save", command=flight_update)
        f_save_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=145)

        conn.commit()
        conn.close()

    # Ticket function to Show, Edit & Delete
    def ticket_show():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # Show database
        cur.execute("SELECT * FROM TICKET")
        tickets = cur.fetchall()

        # print_record = ''
        # for record in records:
        #     print_record += str(record) + "\n"
        #
        # show_label = Label(flight_show, text=print_record)
        # show_label.grid(row=10, column=0, columnspan=2)

        all_tickets_window = Toplevel()
        all_tickets_window.title("All tickets information")

        all_tickets_table_view = ttk.Treeview(all_tickets_window)

        # User Interface Section
        # Define column
        all_tickets_table_view['columns'] = ("Ticket ID", "Emp ID", "Pass ID", "Flight ID", "Seat Type", "Total Cost")

        # Format columns
        all_tickets_table_view.column("#0", width=0, stretch=NO)
        all_tickets_table_view.column("Ticket ID", anchor=W, width=80)
        all_tickets_table_view.column("Emp ID", anchor=W, width=80)
        all_tickets_table_view.column("Pass ID", anchor=CENTER, width=100)
        all_tickets_table_view.column("Flight ID", anchor=CENTER, width=80)
        all_tickets_table_view.column("Seat Type", anchor=CENTER, width=80)
        all_tickets_table_view.column("Total Cost", anchor=CENTER, width=80)

        # Create heading
        all_tickets_table_view.heading("#0", text="", anchor=W)
        all_tickets_table_view.heading("Ticket ID", text="Ticket ID", anchor=CENTER)
        all_tickets_table_view.heading("Emp ID", text="Emp ID", anchor=CENTER)
        all_tickets_table_view.heading("Pass ID", text="Pass ID", anchor=CENTER)
        all_tickets_table_view.heading("Flight ID", text="Flight ID", anchor=CENTER)
        all_tickets_table_view.heading("Seat Type", text="Seat Type", anchor=CENTER)
        all_tickets_table_view.heading("Total Cost", text="Total Cost", anchor=CENTER)

        count = 0
        for ticket in tickets:
            all_tickets_table_view.insert(parent='', index='end', iid=str(count), text="", values=(str(ticket[0]),
                                                                                                  str(ticket[1]),
                                                                                                  str(ticket[2]),
                                                                                                  str(ticket[3]),
                                                                                                  str(ticket[4]),
                                                                                                  str(ticket[5])))
            count += 1

        all_tickets_table_view.pack(padx=20, pady=20)

        conn.commit()
        conn.close()

    def ticket_delete():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # delete
        cur.execute("DELETE FROM TICKET WHERE TICKETID=" + "\'" + (ticket_entry0.get()) + "\'")

        ticket_entry0.delete(0, END)

        conn.commit()
        conn.close()

    def ticket_update():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        cur.execute("UPDATE TICKET SET "
                    "TICKETID = %s, "
                    "EMPID = %s, "
                    "PASSID = %s, "
                    "FLIGHTID = %s, "
                    "SEATTYPE = %s, "
                    "TOTALCOST = %s "
                    "WHERE TICKETID=" + "\'" + (ticket_entry0_editor.get()) + "\'",
                    (
                        ticket_entry0_editor.get(),
                        ticket_entry1_editor.get(),
                        ticket_entry2_editor.get(),
                        ticket_entry3_editor.get(),
                        ticket_entry4_editor.get(),
                        ticket_entry5_editor.get()
                    ))

        conn.commit()
        conn.close()
        ticket_editor.destroy()

    def ticket_edit():
        global ticket_editor
        ticket_editor = Toplevel(window)
        ticket_editor.title('Update Ticket')
        ticket_editor.geometry("400x300")

        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # Edit plane
        cur.execute("SELECT * FROM TICKET WHERE TICKETID=" + "\'" + (ticket_entry0.get()) + "\'")
        ticket_records = cur.fetchall()

        # define global var
        global ticket_entry0_editor
        global ticket_entry1_editor
        global ticket_entry2_editor
        global ticket_entry3_editor
        global ticket_entry4_editor
        global ticket_entry5_editor

        # ticket textbox
        ticket_entry0_editor = Entry(ticket_editor, width=30)
        ticket_entry0_editor.grid(row=0, column=1, padx=20)
        ticket_entry1_editor = Entry(ticket_editor, width=30)
        ticket_entry1_editor.grid(row=1, column=1, padx=20)
        ticket_entry2_editor = Entry(ticket_editor, width=30)
        ticket_entry2_editor.grid(row=2, column=1, padx=20)
        ticket_entry3_editor = Entry(ticket_editor, width=30)
        ticket_entry3_editor.grid(row=3, column=1, padx=20)
        ticket_entry4_editor = Entry(ticket_editor, width=30)
        ticket_entry4_editor.grid(row=4, column=1, padx=20)
        ticket_entry5_editor = Entry(ticket_editor, width=30)
        ticket_entry5_editor.grid(row=5, column=1, padx=20)


        # ticket insert textbox label
        ticket_label0_editor = Label(ticket_editor, text="Ticket ID")
        ticket_label0_editor.grid(row=0, column=0)
        ticket_label1_editor = Label(ticket_editor, text="Employee ID")
        ticket_label1_editor.grid(row=1, column=0)
        ticket_label2_editor = Label(ticket_editor, text="Passenger ID")
        ticket_label2_editor.grid(row=2, column=0)
        ticket_label3_editor = Label(ticket_editor, text="Flight ID")
        ticket_label3_editor.grid(row=3, column=0)
        ticket_label4_editor = Label(ticket_editor, text="Seat Type")
        ticket_label4_editor.grid(row=4, column=0)
        ticket_label5_editor = Label(ticket_editor, text="Total Cost")
        ticket_label5_editor.grid(row=5, column=0)

        # Insert default value
        for record in ticket_records:
            ticket_entry0_editor.insert(0, record[0])
            ticket_entry1_editor.insert(0, record[2])
            ticket_entry2_editor.insert(0, record[2])
            ticket_entry3_editor.insert(0, record[3])
            ticket_entry4_editor.insert(0, record[4])
            ticket_entry5_editor.insert(0, record[5])

        # ticket update Save button
        t_save_btn = Button(ticket_editor, text="Save", command=ticket_update)
        t_save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=145)

        conn.commit()
        conn.close()


    # Employee function to Add Show Delete & Update
    def employee_submit():
        # create database connection
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # Insert into table
        cur.execute("INSERT INTO EMPLOYEE VALUES(%s, %s, %s, %s, %s)",
                    (
                        employee_entry0.get(),
                        employee_entry1.get(),
                        employee_entry2.get(),
                        employee_entry3.get(),
                        employee_entry4.get()
                    ))

        conn.commit()
        conn.close()

        # clear current type in content
        employee_entry0.delete(0, END)
        employee_entry1.delete(0, END)
        employee_entry2.delete(0, END)
        employee_entry3.delete(0, END)
        employee_entry4.delete(0, END)

    def employee_show():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # Show database
        cur.execute("SELECT * FROM EMPLOYEE")
        employees = cur.fetchall()

        # print_record = ''
        # for record in records:
        #     print_record += str(record) + "\n"
        #
        # show_label = Label(flight_show, text=print_record)
        # show_label.grid(row=10, column=0, columnspan=2)

        all_employee_window = Toplevel()
        all_employee_window.title("All employees information")

        all_employees_table_view = ttk.Treeview(all_employee_window)

        # User Interface Section
        # Define column
        all_employees_table_view['columns'] = ("Emp ID", "Emp Name", "Emp Add", "Phone Num", "Position")

        # Format columns
        all_employees_table_view.column("#0", width=0, stretch=NO)
        all_employees_table_view.column("Emp ID", anchor=W, width=80)
        all_employees_table_view.column("Emp Name", anchor=W, width=80)
        all_employees_table_view.column("Emp Add", anchor=CENTER, width=100)
        all_employees_table_view.column("Phone Num", anchor=CENTER, width=80)
        all_employees_table_view.column("Position", anchor=CENTER, width=80)

        # Create heading
        all_employees_table_view.heading("#0", text="", anchor=W)
        all_employees_table_view.heading("Emp ID", text="Emp ID", anchor=CENTER)
        all_employees_table_view.heading("Emp Name", text="Emp Name", anchor=CENTER)
        all_employees_table_view.heading("Emp Add", text="Emp Add", anchor=CENTER)
        all_employees_table_view.heading("Phone Num", text="Phone Num", anchor=CENTER)
        all_employees_table_view.heading("Position", text="Position", anchor=CENTER)

        count = 0
        for employee in employees:
            all_employees_table_view.insert(parent='', index='end', iid=str(count), text="", values=(str(employee[0]),
                                                                                                  str(employee[1]),
                                                                                                  str(employee[2]),
                                                                                                  str(employee[3]),
                                                                                                  str(employee[4])))
            count += 1

        all_employees_table_view.pack(padx=20, pady=20)

        conn.commit()
        conn.close()

    def employee_delete():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # delete
        cur.execute("DELETE FROM EMPLOYEE WHERE EMPID=" + "\'" + (employee_entry5.get()) + "\'")

        employee_entry5.delete(0, END)

        conn.commit()
        conn.close()

    def employee_update():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        cur.execute("UPDATE EMPLOYEE SET "
                    "EMPID = %s, "
                    "EMPNAME = %s, "
                    "EMPADD = %s, "
                    "EMPPHONENUM = %s, "
                    "EMPPOSITION = %s "
                    "WHERE EMPID=" + "\'" + (e_entry0_editor.get()) + "\'",
                    (
                        e_entry0_editor.get(),
                        e_entry1_editor.get(),
                        e_entry2_editor.get(),
                        e_entry3_editor.get(),
                        e_entry4_editor.get()
                    ))

        conn.commit()
        conn.close()
        employee_editor.destroy()

    def employee_edit():
        global employee_editor
        employee_editor = Toplevel(window)
        employee_editor.title('Update Employee')
        employee_editor.geometry("400x300")

        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # Edit plane
        cur.execute("SELECT * FROM EMPLOYEE WHERE EMPID=" + "\'" + (employee_entry5.get()) + "\'")
        employee_records = cur.fetchall()

        # define global var
        global e_entry0_editor
        global e_entry1_editor
        global e_entry2_editor
        global e_entry3_editor
        global e_entry4_editor

        # Plane textbox
        e_entry0_editor = Entry(employee_editor, width=30)
        e_entry0_editor.grid(row=0, column=1, padx=20)
        e_entry1_editor = Entry(employee_editor, width=30)
        e_entry1_editor.grid(row=1, column=1, padx=20)
        e_entry2_editor = Entry(employee_editor, width=30)
        e_entry2_editor.grid(row=2, column=1, padx=20)
        e_entry3_editor = Entry(employee_editor, width=30)
        e_entry3_editor.grid(row=3, column=1, padx=20)
        e_entry4_editor = Entry(employee_editor, width=30)
        e_entry4_editor.grid(row=4, column=1, padx=20)


        # Plane insert textbox label
        e_label0_editor = Label(employee_editor, text="Employee ID")
        e_label0_editor.grid(row=0, column=0)
        e_label1_editor = Label(employee_editor, text="Employee Name")
        e_label1_editor.grid(row=1, column=0)
        e_label2_editor = Label(employee_editor, text="Address")
        e_label2_editor.grid(row=2, column=0)
        e_label3_editor = Label(employee_editor, text="Phone Number")
        e_label3_editor.grid(row=3, column=0)
        e_label4_editor = Label(employee_editor, text="Position")
        e_label4_editor.grid(row=4, column=0)

        # Insert default value
        for record in employee_records:
            e_entry0_editor.insert(0, record[0])
            e_entry1_editor.insert(0, record[1])
            e_entry2_editor.insert(0, record[2])
            e_entry3_editor.insert(0, record[3])
            e_entry4_editor.insert(0, record[4])

        # Plane update Save button
        e_save_btn = Button(employee_editor, text="Save", command=employee_update)
        e_save_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=145)

        conn.commit()
        conn.close()

    # Passenger function to Add Show Delete & Update
    def passenger_submit():
        # create database connection
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # Insert into table
        cur.execute("INSERT INTO PASSENGER VALUES(%s, %s, %s, %s, %s)",
                    (
                        passenger_entry0.get(),
                        passenger_entry1.get(),
                        passenger_entry2.get(),
                        passenger_entry3.get(),
                        passenger_entry4.get()
                    ))

        conn.commit()
        conn.close()

        # clear current type in content
        passenger_entry0.delete(0, END)
        passenger_entry1.delete(0, END)
        passenger_entry2.delete(0, END)
        passenger_entry3.delete(0, END)
        passenger_entry4.delete(0, END)

    def passenger_show():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # Show database
        cur.execute("SELECT * FROM PASSENGER")
        passengers = cur.fetchall()

        # print_record = ''
        # for record in records:
        #     print_record += str(record) + "\n"
        #
        # show_label = Label(flight_show, text=print_record)
        # show_label.grid(row=10, column=0, columnspan=2)

        all_passengers_window = Toplevel()
        all_passengers_window.title("All passengers information")

        all_passengers_table_view = ttk.Treeview(all_passengers_window)

        # User Interface Section
        # Define column
        all_passengers_table_view['columns'] = ("Pass ID", "Pass Name", "Phone", "Add", "IDNo")

        # Format columns
        all_passengers_table_view.column("#0", width=0, stretch=NO)
        all_passengers_table_view.column("Pass ID", anchor=W, width=80)
        all_passengers_table_view.column("Pass Name", anchor=W, width=80)
        all_passengers_table_view.column("Phone", anchor=CENTER, width=100)
        all_passengers_table_view.column("Add", anchor=CENTER, width=80)
        all_passengers_table_view.column("IDNo", anchor=CENTER, width=80)

        # Create heading
        all_passengers_table_view.heading("#0", text="", anchor=W)
        all_passengers_table_view.heading("Pass ID", text="Pass ID", anchor=CENTER)
        all_passengers_table_view.heading("Pass Name", text="Pass Name", anchor=CENTER)
        all_passengers_table_view.heading("Phone", text="Phone", anchor=CENTER)
        all_passengers_table_view.heading("Add", text="Add", anchor=CENTER)
        all_passengers_table_view.heading("IDNo", text="IDNo", anchor=CENTER)

        count = 0
        for passenger in passengers:
            all_passengers_table_view.insert(parent='', index='end', iid=str(count), text="", values=(str(passenger[0]),
                                                                                                  str(passenger[1]),
                                                                                                  str(passenger[2]),
                                                                                                  str(passenger[3]),
                                                                                                  str(passenger[4])))
            count += 1

        all_passengers_table_view.pack(padx=20, pady=20)

        conn.commit()
        conn.close()

    def passenger_delete():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # delete
        cur.execute("DELETE FROM PASSENGER WHERE PASSID=" + "\'" + (passenger_entry5.get()) + "\'")

        passenger_entry5.delete(0, END)

        conn.commit()
        conn.close()

    def passenger_update():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        cur.execute("UPDATE PASSENGER SET "
                    "PASSID = %s, "
                    "PASSNAME = %s, "
                    "PASSPHONENUMBER = %s, "
                    "PASSADDRESS = %s, "
                    "PASSIDNO = %s "
                    "WHERE PASSID=" + "\'" + (pass_entry0_editor.get()) + "\'",
                    (
                        pass_entry0_editor.get(),
                        pass_entry1_editor.get(),
                        pass_entry2_editor.get(),
                        pass_entry3_editor.get(),
                        pass_entry4_editor.get()
                    ))

        conn.commit()
        conn.close()
        passenger_editor.destroy()

    def passenger_edit():
        global passenger_editor
        passenger_editor = Toplevel(window)
        passenger_editor.title('Update Passenger')
        passenger_editor.geometry("400x300")

        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        # Edit plane
        cur.execute("SELECT * FROM PASSENGER WHERE PASSID=" + "\'" + (passenger_entry5.get()) + "\'")
        passenger_records = cur.fetchall()

        # define global var
        global pass_entry0_editor
        global pass_entry1_editor
        global pass_entry2_editor
        global pass_entry3_editor
        global pass_entry4_editor

        # Plane textbox
        pass_entry0_editor = Entry(passenger_editor, width=30)
        pass_entry0_editor.grid(row=0, column=1, padx=20)
        pass_entry1_editor = Entry(passenger_editor, width=30)
        pass_entry1_editor.grid(row=1, column=1, padx=20)
        pass_entry2_editor = Entry(passenger_editor, width=30)
        pass_entry2_editor.grid(row=2, column=1, padx=20)
        pass_entry3_editor = Entry(passenger_editor, width=30)
        pass_entry3_editor.grid(row=3, column=1, padx=20)
        pass_entry4_editor = Entry(passenger_editor, width=30)
        pass_entry4_editor.grid(row=4, column=1, padx=20)


        # Plane insert textbox label
        pass_label0_editor = Label(passenger_editor, text="Passenger ID")
        pass_label0_editor.grid(row=0, column=0)
        pass_label1_editor = Label(passenger_editor, text="Passenger Name")
        pass_label1_editor.grid(row=1, column=0)
        pass_label2_editor = Label(passenger_editor, text="Phone Number")
        pass_label2_editor.grid(row=2, column=0)
        pass_label3_editor = Label(passenger_editor, text="Address")
        pass_label3_editor.grid(row=3, column=0)
        pass_label4_editor = Label(passenger_editor, text="Identify Number")
        pass_label4_editor.grid(row=4, column=0)

        # Insert default value
        for record in passenger_records:
            pass_entry0_editor.insert(0, record[0])
            pass_entry1_editor.insert(0, record[1])
            pass_entry2_editor.insert(0, record[2])
            pass_entry3_editor.insert(0, record[3])
            pass_entry4_editor.insert(0, record[4])

        # Plane update Save button
        e_save_btn = Button(passenger_editor, text="Save", command=passenger_update)
        e_save_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=145)

        conn.commit()
        conn.close()

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

        plane_seat2_entry_img = PhotoImage(file=f"img/Plane/img_textBox4.png")
        plane_seat1_entry_bg = plane_canvas.create_image(
            405.5, 323.5,
            image=plane_seat1_entry_img)

        plane_seat2_entry = Entry(
            plane_window,
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0)

        plane_seat2_entry.place(
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
            command=plane_edit,
            relief="flat")

        plane_b2.place(
            x=83, y=741,
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
        global flight_entry0
        global flight_entry1
        global flight_entry2
        global flight_entry3
        global flight_entry4
        global flight_entry5
        global flight_entry6
        global flight_entry7
        global flight_entry8
        global flight_entry9
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
            command=flight_submit,
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
            command=flight_show,
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
            command=flight_edit,
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
            command=flight_delete,
            relief="flat")

        flight_b3.place(
            x=308, y=741,
            width=187,
            height=62)

    def ticket_management_click():
        ticket_window = Toplevel(window)

        global ticket_background_img
        global ticket_entry0
        global ticket_img0
        global ticket_img1
        global ticket_img2

        ticket_window.geometry("600x400")
        ticket_window.configure(bg="#000000")
        ticket_window.title('Ticket Management')
        ticket_canvas = Canvas(
            ticket_window,
            bg="#000000",
            height=400,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        ticket_canvas.place(x=0, y=0)

        ticket_background_img = PhotoImage(file=f"img/e_ticket/background.png")
        ticket_background = ticket_canvas.create_image(
            359.0, 358.0,
            image=ticket_background_img)

        ticket_img0 = PhotoImage(file=f"img/e_ticket/img0.png")
        ticket_b0 = Button(
            ticket_window,
            image=ticket_img0,
            borderwidth=0,
            highlightthickness=0,
            command=ticket_show,
            relief="flat")

        ticket_b0.place(
            x=195, y=71,
            width=187,
            height=62)

        ticket_entry0_img = PhotoImage(file=f"img/e_ticket/img_textBox0.png")
        ticket_entry0_bg = ticket_canvas.create_image(
            290.0, 199.5,
            image=ticket_entry0_img)

        ticket_entry0 = Entry(
            ticket_window,
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0)

        ticket_entry0.place(
            x=82, y=181,
            width=416,
            height=35)

        ticket_img1 = PhotoImage(file=f"img/e_ticket/img1.png")
        ticket_b1 = Button(
            ticket_window,
            image=ticket_img1,
            borderwidth=0,
            highlightthickness=0,
            command=ticket_edit,
            relief="flat")

        ticket_b1.place(
            x=83, y=266,
            width=187,
            height=62)

        ticket_img2 = PhotoImage(file=f"img/e_ticket/img2.png")
        ticket_b2 = Button(
            ticket_window,
            image=ticket_img2,
            borderwidth=0,
            highlightthickness=0,
            command=ticket_delete,
            relief="flat")

        ticket_b2.place(
            x=308, y=266,
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
        global employee_entry0
        global employee_entry1
        global employee_entry2
        global employee_entry3
        global employee_entry4
        global employee_entry5
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
            command=employee_submit,
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
            command=employee_show,
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
            command=employee_edit,
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
            command=employee_delete,
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
        global passenger_entry0
        global passenger_entry1
        global passenger_entry2
        global passenger_entry3
        global passenger_entry4
        global passenger_entry5
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
            command=passenger_submit,
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
            command=passenger_show,
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
            command=passenger_edit,
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
            command=passenger_delete,
            relief="flat")

        b3.place(
            x=308, y=741,
            width=187,
            height=62)

    background_img = PhotoImage(file=f"img/AirportManagement/background.png")
    background = canvas.create_image(
        808.0, 229.0,
        image=background_img)

    img0 = PhotoImage(file=f"img/AirportManagement/img0.png")
    passenger_button = Button(
        window,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=passenger_management_click,
        relief="flat")

    passenger_button.place(
        x=828, y=547,
        width=338,
        height=66)

    img1 = PhotoImage(file=f"img/AirportManagement/img1.png")
    employee_button = Button(
        window,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=employee_management_click,
        relief="flat")

    employee_button.place(
        x=830, y=453,
        width=337,
        height=69)

    img2 = PhotoImage(file=f"img/AirportManagement/img2.png")
    ticket_button = Button(
        window,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=ticket_management_click,
        relief="flat")

    ticket_button.place(
        x=830, y=363,
        width=338,
        height=66)

    img3 = PhotoImage(file=f"img/AirportManagement/img3.png")
    flight_button = Button(
        window,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=flight_management_click,
        relief="flat")

    flight_button.place(
        x=828, y=268,
        width=338,
        height=66)

    img4 = PhotoImage(file=f"img/AirportManagement/img4.png")
    plane_button = Button(
        window,
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=plane_management_click,
        relief="flat")

    plane_button.place(
        x=828, y=178,
        width=338,
        height=66)
