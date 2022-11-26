from tkinter import *


def passenger_management_ui(inputID):
    from tkinter import ttk
    from tkinter import messagebox
    import random
    import sys
    import mysql.connector

    ticket_window = Toplevel()

    ticket_window.geometry("600x900")
    ticket_window.configure(bg="#9ba4b4")
    ticket_window.title("Booking")
    ticket_canvas = Canvas(
        ticket_window,
        bg="#9ba4b4",
        height=900,
        width=600,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    ticket_canvas.place(x=0, y=0)

    global background_img
    global entry0_img
    global entry1_img
    global entry2_img
    global entry3_img
    global entry4_img
    global entry6_img
    global img0
    global img1

    def btn_clicked():
        print("Button Clicked")

    def message_no_avaiable_flight():
        messagebox.showinfo("Error!", "Sorry! No available flight at this time or location.")

    def message_successful_booked():
        messagebox.showinfo("SUCCESSFULLY BOOKED!", "Successfully booked!")

    def message_error_transaction(error):
        messagebox.showerror(f"ERROR!", "Something went wrong. \n"
                                        "Please try again!")

    def message_fully_booked_flight(available_seats, seat_type, number_pas):
        messagebox.showinfo(
            f"[ERROR 102]! OUT OF SEAT, AVAILABLE SEAT {available_seats[seat_type - 1]} BUT YOU NEED {number_pas}. \n"
            f"TRY ANOTHER TYPE OF SEAT OR FLIGHT. THANKS!")

    def get_flight_info_by_date(origin, dest, depart_date, arrival_date):
        try:
            connect = mysql.connector.connect(
                user="root",
                password="FzrTscd0aGODkVIUXtsa",
                host="containers-us-west-44.railway.app",
                port=5960,
                database="railway"
            )

            cursor = connect.cursor()
        except mysql.connector.Error as e:
            print(f"Error connecting to Mysql Platform: {e}")
            connect.rollback()
            sys.exit(1)

        cursor.execute("SELECT * FROM FLIGHT "
                       "WHERE ORIGIN=%s AND DESTINATION=%s AND DEPARTURE_DATE=%s AND ARRIVAL_DATE=%s",
                       (origin, dest, depart_date, arrival_date,))
        flights = cursor.fetchall()
        if not flights:
            return None
        else:
            return flights

    def check_available_seat(number_pas, seat_type, available_seats):
        if seat_type == 1:
            if number_pas <= available_seats[0]:
                return True
            else:
                return False
        elif seat_type == 2:
            if number_pas <= available_seats[1]:
                return True
            else:
                return False

    def create_ticket_id(chosen_flight_id, pas_id, pas_name, number_pas, origin, destination):
        return chosen_flight_id[-3:] + pas_id[-3:] + pas_name.strip().replace(" ", "")[:3] + str(number_pas) + origin[
                                                                                                               :2] \
               + destination[:2] + str(random.randint(10000, 99999))

    def dist(origin, destination):
        domestic_airport_code = ["HAN", "SGN", "DAD", "VDO", "HPH", "VII", "HUI", "CXR", "DLI", "PQC", "UIH", "VCA"]
        if origin in domestic_airport_code and destination in domestic_airport_code:
            return 2000
        return 5500

    def get_ticket_price(seat_type, number_pas, origin, destination, depart_date, return_date, round_trip):
        total = 0
        fix_cost_seat_type1 = 30000  # made this up
        fix_cost_seat_type2 = 15000
        fuel_cost = 30000  # google this
        services = 2000  # magic number :v
        tax = int((number_pas * fix_cost_seat_type1 + dist(origin, destination) * fuel_cost + services) * 10 / 100)

        if seat_type == 1:
            total = number_pas * fix_cost_seat_type1 + dist(origin, destination) * fuel_cost + services + tax
        elif seat_type == 2:
            total = number_pas * fix_cost_seat_type2 + dist(origin, destination) * fuel_cost + services + tax
        if round_trip:
            return total * 2
        return total

    def show_available_flight():
        origin = entry1.get()
        destination = entry4.get()
        depart_date = entry2.get()
        arrival_date = entry3.get()

        flights = get_flight_info_by_date(origin, destination, depart_date, arrival_date)
        if not flights:
            message_no_avaiable_flight()
        else:
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
            all_flight_table_view.column("Departure Date", anchor=CENTER, width=80)
            all_flight_table_view.column("Arrival Date", anchor=CENTER, width=80)
            all_flight_table_view.column("Origin", anchor=CENTER, width=80)
            all_flight_table_view.column("Destination", anchor=CENTER, width=60)
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
                                                                                                      str(flight[4]),
                                                                                                      str(flight[5]),
                                                                                                      str(flight[6]),
                                                                                                      str(flight[7]),))
                count += 1

            all_flight_table_view.pack(padx=20, pady=20)

    def create_ticket():
        # Get all input values to variables
        chosen_flight_id = entry6.get()
        pas_id = inputID
        pas_name = entry0.get()
        number_pas = int(noOfPax.get())
        seat_type = int(seatType.get())
        origin = entry1.get()
        destination = entry4.get()
        depart_date = entry2.get()
        arrival_date = entry3.get()
        round_trip = False

        # Find flight that match 4 categories: origin, destination, depart date, arrival date
        flights = get_flight_info_by_date(origin, destination, depart_date, arrival_date)

        # Pick the chosen flight, this will return a tuple
        chosen_flight = [flight for flight in flights if chosen_flight_id == flight[0]]

        # Choose the index 6 and 7 which are available seat type 1 and type 2, respectively.
        available_seats = [chosen_flight[0][6], chosen_flight[0][7]]

        if check_available_seat(number_pas, seat_type, available_seats):
            try:
                conn = mysql.connector.connect(
                    user="root",
                    password="FzrTscd0aGODkVIUXtsa",
                    host="containers-us-west-44.railway.app",
                    port=5960,
                    database="railway"
                )
                cur = conn.cursor()
                conn.autocommit = False
                conn.start_transaction(consistent_snapshot=False,
                                       isolation_level='SERIALIZABLE',
                                       readonly=False)

                total_cost = 0
                ticket_id = create_ticket_id(chosen_flight_id, pas_id, pas_name, number_pas, origin, destination)
                total_cost = get_ticket_price(seat_type, number_pas, origin, destination, depart_date, arrival_date,
                                              round_trip)

                cur.execute("INSERT INTO TICKET(TICKETID, PASSID, FLIGHTID, SEATTYPE, TOTALCOST) "
                            "VALUES (%s, %s, %s, %s, %s)",
                            (ticket_id, pas_id, chosen_flight_id, seat_type, total_cost,))
                if seat_type == 1:
                    cur.execute("UPDATE FLIGHT SET QUANTITY_SEAT1=%s WHERE FLIGHTID=%s",
                                (available_seats[0] - number_pas, chosen_flight_id))
                elif seat_type == 2:
                    cur.execute("UPDATE FLIGHT SET QUANTITY_SEAT2=%s WHERE FLIGHTID=%s",
                                (available_seats[1] - number_pas, chosen_flight_id))
                conn.commit()

                message_successful_booked()
            except mysql.connector.Error as error:
                message_error_transaction(error)
                conn.rollback()

        else:
            message_fully_booked_flight(available_seats, seat_type, number_pas)

    # Drop down menu for number of passenger (No of pax)
    noOfPaxOptions = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    noOfPax = StringVar()
    noOfPax.set(noOfPaxOptions[0])
    dropNoOfPax = OptionMenu(ticket_window, noOfPax, *noOfPaxOptions)
    dropDownIcon = PhotoImage(file=f"img/ticket/drop-down1.png")
    dropNoOfPax.config(indicatoron=False, compound=RIGHT, image=dropDownIcon, width=100, background='#D9D9D9',
                       activebackground='#fff')
    dropNoOfPax.place(
        x=83, y=153,
        width=50,
        height=30
    )

    # Drop down menu for seat type (1: Bussiness class, 2: Economy class)
    seatTypeOptions = ["1", "2"]
    seatType = StringVar()
    seatType.set(seatTypeOptions[1])
    dropSeatType = OptionMenu(ticket_window, seatType, *seatTypeOptions)
    dropSeatIcon = PhotoImage(file=f"img/ticket/drop-down1.png")
    dropSeatType.config(indicatoron=False, compound=RIGHT, image=dropSeatIcon, width=100, background='#D9D9D9',
                        activebackground='#fff')
    dropSeatType.place(
        x=185, y=153,
        width=50,
        height=30
    )

    # User interface section
    background_img = PhotoImage(file=f"img/ticket/background.png")
    background = ticket_canvas.create_image(
        165.0, 423.5,
        image=background_img)

    entry0_img = PhotoImage(file=f"img/ticket/img_textBox0.png")
    entry0_bg = ticket_canvas.create_image(
        290.0, 91.5,
        image=entry0_img)

    entry0 = Entry(
        ticket_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry0.place(
        x=82, y=73,
        width=416,
        height=35)

    entry1_img = PhotoImage(file=f"img/ticket/img_textBox1.png")
    entry1_bg = ticket_canvas.create_image(
        176.5, 245.5,
        image=entry1_img)

    entry1 = Entry(
        ticket_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry1.place(
        x=83, y=228,
        width=187,
        height=33)

    entry2_img = PhotoImage(file=f"img/ticket/img_textBox2.png")
    entry2_bg = ticket_canvas.create_image(
        177.5, 332.5,
        image=entry2_img)

    entry2 = Entry(
        ticket_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry2.place(
        x=84, y=315,
        width=187,
        height=33)

    entry3_img = PhotoImage(file=f"img/ticket/img_textBox3.png")
    entry3_bg = ticket_canvas.create_image(
        404.5, 332.5,
        image=entry3_img)

    entry3 = Entry(
        ticket_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry3.place(
        x=311, y=315,
        width=187,
        height=33)

    entry4_img = PhotoImage(file=f"img/ticket/img_textBox4.png")
    entry4_bg = ticket_canvas.create_image(
        403.5, 247.5,
        image=entry4_img)

    entry4 = Entry(
        ticket_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry4.place(
        x=310, y=229,
        width=187,
        height=35)

    # entry5_img = PhotoImage(file=f"img/ticket/img_textBox5.png")
    # entry5_bg = ticket_canvas.create_image(
    #     290.0, 418.5,
    #     image=entry5_img)
    #
    # entry5 = Entry(
    #     ticket_window,
    #     bd=0,
    #     bg="#d9d9d9",
    #     highlightthickness=0)
    #
    # entry5.place(
    #     x=82, y=400,
    #     width=416,
    #     height=35)

    # entry6_img = PhotoImage(file=f"img/ticket/img_textBox6.png")
    # entry6_bg = ticket_canvas.create_image(
    #     291.0, 577,
    #     image=entry6_img)

    entry6 = Entry(
        ticket_window,
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0)

    entry6.place(
        x=83, y=504,
        width=416,
        height=35)

    img0 = PhotoImage(file=f"img/ticket/img0.png")
    b0 = Button(
        ticket_window,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=show_available_flight,
        relief="flat")

    b0.place(
        x=142, y=397,
        width=293,
        height=62)

    img1 = PhotoImage(file=f"img/ticket/img1.png")
    b1 = Button(
        ticket_window,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=create_ticket,
        relief="flat")

    b1.place(
        x=143, y=577,
        width=293,
        height=62)

    ticket_window.resizable(False, False)
    ticket_window.mainloop()

