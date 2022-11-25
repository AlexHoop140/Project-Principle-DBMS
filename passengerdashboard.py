from tkinter import *


def passenger_management_ui(inputID, inputPassword):
    from tkinter import Entry, Toplevel, Canvas, Tk, PhotoImage, Button
    from tkinter import ttk
    from tkinter import messagebox
    import mysql.connector
    import booking as bk

    window = Toplevel()

    window.geometry("1280x720")
    window.configure(bg="#ffffff")
    window.title("Passenger Dashboard")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    def user_exist_popup():
        messagebox.showinfo("Error!", "Sorry, Passenger is not existed!")

    def btn_ticket():
        bk.passenger_management_ui(inputID)

    def btn_flight():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        passid = inputID
        # Get passenger info
        cur.execute("SELECT T.TICKETID, PASSNAME, T.FLIGHTID, SEATTYPE, F.PLANEID, DEPARTURE_DATE, ARRIVAL_DATE, ORIGIN, DESTINATION, TOTALCOST "
                    "FROM TICKET T INNER JOIN FLIGHT F ON T.FLIGHTID=F.FLIGHTID INNER JOIN PASSENGER P ON T.PASSID=P.PASSID "
                    "WHERE T.PASSID=%s ", (str(passid),))
        flights_info = cur.fetchall()

        conn.close()

        flight_show = Toplevel()
        flight_show.title("All of your flights information")

        all_flight_view = ttk.Treeview(flight_show)

        # Define column
        all_flight_view['columns'] = ("Ticket ID", "Passenger Name", "Flight ID", "Seat Type", "Plane ID",
                                      "Departure Date", "Arrival Date", "Origin", "Destination", "Total Cost")

        # Format columns
        all_flight_view.column("#0", width=0, stretch=NO)
        all_flight_view.column("Ticket ID", anchor=W, width=140)
        all_flight_view.column("Passenger Name", anchor=W, width=150)
        all_flight_view.column("Flight ID", anchor=CENTER, width=80)
        all_flight_view.column("Seat Type", anchor=CENTER, width=60)
        all_flight_view.column("Plane ID", anchor=CENTER, width=80)
        all_flight_view.column("Departure Date", anchor=CENTER, width=80)
        all_flight_view.column("Arrival Date", anchor=CENTER, width=80)
        all_flight_view.column("Origin", anchor=CENTER, width=60)
        all_flight_view.column("Destination", anchor=CENTER, width=60)
        all_flight_view.column("Total Cost", anchor=E, width=120)

        # Create heading
        all_flight_view.heading("#0", text="", anchor=W)
        all_flight_view.heading("Ticket ID", text="Ticket ID", anchor=W)
        all_flight_view.heading("Passenger Name", text="Passenger Name", anchor=CENTER)
        all_flight_view.heading("Flight ID", text="Flight ID", anchor=CENTER)
        all_flight_view.heading("Seat Type", text="Seat Type", anchor=CENTER)
        all_flight_view.heading("Plane ID", text="Plane ID", anchor=CENTER)
        all_flight_view.heading("Departure Date", text="Departure Dater", anchor=CENTER)
        all_flight_view.heading("Arrival Date", text="Arrival Date", anchor=CENTER)
        all_flight_view.heading("Origin", text="Origin", anchor=CENTER)
        all_flight_view.heading("Destination", text="Destination", anchor=CENTER)
        all_flight_view.heading("Total Cost", text="Total Cost", anchor=CENTER)

        count = 0
        for flight in flights_info:
            all_flight_view.insert(parent='', index='end', iid=str(count), text="", values=(str(flight[0]),
                                                                                            str(flight[1]),
                                                                                            str(flight[2]),
                                                                                            str(flight[3]),
                                                                                            str(flight[4]),
                                                                                            str(flight[5]),
                                                                                            str(flight[6]),
                                                                                            str(flight[7]),
                                                                                            str(flight[8]),
                                                                                            str(flight[9])+" VND",))
            count += 1

        all_flight_view.pack(padx=20, pady=20)

    def profile_show(passid):
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()
        passid = inputID
        # Get passenger info
        cur.execute("SELECT * FROM PASSENGER WHERE PASSID=%s", (passid,))
        passenger_info = cur.fetchall()

        conn.close()

        profile_show_window = Toplevel()

        passenger_view = ttk.Treeview(profile_show_window)

        # Define column
        passenger_view['columns'] = ("Passenger ID", "Passenger Name", "Phone Number", "Address", "ID Number")

        # Format columns
        passenger_view.column("#0", width=0, stretch=NO)
        passenger_view.column("Passenger ID", anchor=W, width=80)
        passenger_view.column("Passenger Name", anchor=CENTER, width=120)
        passenger_view.column("Phone Number", anchor=E, width=120)
        passenger_view.column("Address", anchor=E, width=80)
        passenger_view.column("ID Number", anchor=E, width=80)

        # Create heading
        passenger_view.heading("#0", text="", anchor=W)
        passenger_view.heading("Passenger ID", text="Passenger ID", anchor=W)
        passenger_view.heading("Passenger Name", text="Passenger Name", anchor=CENTER)
        passenger_view.heading("Phone Number", text="Phone Number", anchor=E)
        passenger_view.heading("Address", text="Address", anchor=E)
        passenger_view.heading("ID Number", text="ID Number", anchor=E)

        passenger_view.insert(parent='', index='end', iid="0", text="", values=(str(passenger_info[0][0]),
                                                                                str(passenger_info[0][1]),
                                                                                str(passenger_info[0][2]),
                                                                                str(passenger_info[0][3]),
                                                                                str(passenger_info[0][4]),))

        passenger_view.pack(padx=20, pady=20)

        # show_label = Label(profile_show_window)
        # show_label.grid(row=10, column=0, columnspan=2)

    def update_passenger_info(passengerid, passName, phoneNumber, address, idno):
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        passID = passengerid[0][0]
        cur.execute("UPDATE PASSENGER SET PASSNAME=%s, PASSPHONENUMBER=%s, PASSADDRESS=%s, PASSIDNO=%s WHERE PASSID=%s",
                    (passName, phoneNumber, address, idno, passID))

        conn.commit()
        conn.close()

    def update_passenger_info_window(passenger_info):
        global pax_background_img
        global pax_entry0_img
        global pax_entry1_img
        global pax_entry2_img
        global pax_entry3_img
        global pax_img0
        global pax_img1

        pax_window = Toplevel()

        pax_window.geometry("600x900")
        pax_window.configure(bg="#9ba4b4")
        pax_window.title("Passenger Update Information")
        pax_window.canvas = Canvas(
            pax_window,
            bg="#9ba4b4",
            height=900,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        pax_window.canvas.place(x=0, y=0)

        pax_background_img = PhotoImage(file=f"img/profile/background.png")
        pax_background = pax_window.canvas.create_image(
            165.0, 423.5,
            image=pax_background_img)

        pax_entry0_img = PhotoImage(file=f"img/profile/img_textBox0.png")
        pax_entry0_bg = pax_window.canvas.create_image(
            290.0, 91.5,
            image=pax_entry0_img)

        pax_entry0 = Entry(
            pax_window,
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0)

        pax_entry0.place(
            x=82, y=73,
            width=416,
            height=35)

        pax_entry1_img = PhotoImage(file=f"img/profile/img_textBox1.png")
        entry1_bg = pax_window.canvas.create_image(
            290.0, 169.5,
            image=pax_entry1_img)

        pax_entry1 = Entry(
            pax_window,
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0)

        pax_entry1.place(
            x=82, y=151,
            width=416,
            height=35)

        pax_entry2_img = PhotoImage(file=f"img/profile/img_textBox2.png")
        pax_entry2_bg = pax_window.canvas.create_image(
            291.0, 246.5,
            image=pax_entry2_img)

        pax_entry2 = Entry(
            pax_window,
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0)

        pax_entry2.place(
            x=83, y=228,
            width=416,
            height=35)

        pax_entry3_img = PhotoImage(file=f"img/profile/img_textBox3.png")
        pax_entry3_bg = pax_window.canvas.create_image(
            291.0, 327.5,
            image=pax_entry3_img)

        pax_entry3 = Entry(
            pax_window,
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0)

        pax_entry3.place(
            x=83, y=309,
            width=416,
            height=35)

        pax_img0 = PhotoImage(file=f"img/profile/img0.png")
        pax_b0 = Button(
            pax_window,
            image=pax_img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: update_passenger_info(passenger_info, pax_entry0.get(), pax_entry1.get(), pax_entry2.get(),
                                                  pax_entry3.get()),
            relief="flat")

        pax_b0.place(
            x=144, y=393,
            width=293,
            height=62)

        pax_img1 = PhotoImage(file=f"img/profile/img1.png")
        pax_b1 = Button(
            pax_window,
            image=pax_img1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: profile_show(inputID),
            relief="flat")

        pax_b1.place(
            x=144, y=474,
            width=293,
            height=62)

    def btn_profile():
        conn = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )
        cur = conn.cursor()

        passid = inputID
        # Get passenger info
        cur.execute("SELECT * FROM PASSENGER WHERE PASSID=%s", (passid,))
        passenger_info = cur.fetchall()

        conn.close()

        if len(passenger_info) == 0:
            user_exist_popup()
        else:
            update_passenger_info_window(passenger_info)

    def btn_clicked():
        print("Button Clicked")

    background_img = PhotoImage(file=f"img/dashboard/background.png")
    background = canvas.create_image(
        640.0, 151.0,
        image=background_img)

    img0 = PhotoImage(file=f"img/dashboard/img0.png")
    b0 = Button(
        window,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_ticket,
        relief="flat")

    b0.place(
        x=493, y=269,
        width=298,
        height=47)

    img1 = PhotoImage(file=f"img/dashboard/img1.png")
    b1 = Button(
        window,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=btn_flight,
        relief="flat")

    b1.place(
        x=493, y=355,
        width=298,
        height=47)

    img2 = PhotoImage(file=f"img/dashboard/img2.png")
    b2 = Button(
        window,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_profile,
        relief="flat")

    b2.place(
        x=485, y=438,
        width=306,
        height=47)

    window.resizable(False, False)
    window.mainloop()
