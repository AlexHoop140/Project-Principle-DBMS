from turtle import distance

import mysql.connector
import sys
import random


################# PLANE SECTION ##################

# Insert new plane information
def insert_plane_info(conn, cursor, reg_number, plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer):
    cursor.execute("INSERT INTO PLANES VALUES(%s, %s, %s, %s, %s, %s)",
                   (reg_number, plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer))
    conn.commit()


# Update plane information with registration number
def update_plane_info(conn, cursor, reg_number, plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer):
    cursor.execute(
        "UPDATE PLANES SET PLANEID=%s, TOTALSEAT=%s, TYPE1SEAT=%s, TYPE2SEAT=%s, "
        "MANUFACTURER=%s WHERE PLANEID=%s",
        (plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer, reg_number,))
    conn.commit()


def delete_plane(conn, cursor, plane_id):
    cursor.execute("DELETE FROM PLANES "
                   "WHERE PLANEID=%s", (plane_id,))
    conn.commit()


def show_plane_infor(cursor, plane_id):
    cursor.execute("SELECT * FROM PLANES WHERE PLANEID=%s", (plane_id,))
    planes = cursor.fetchall()
    if not planes:
        print("No plane in database!")
    else:
        for plane in planes:
            print(plane)


##################################################

################# FLIGHT SECTION #################

def insert_flight_info(conn, cursor, flight_id, plane_id, departure_date, arrrival_date, destination, origin, note):
    cursor.execute("INSERT INTO FLIGHT(FLIGHTID, PLANEID, DEPARTURE_DATE, ARRIVAL_DATE, DESTINATION, ORIGIN, "
                   "NOTE) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                       flight_id, plane_id, departure_date, arrrival_date, destination, origin, note))
    cursor.callproc("FILL_AVAILABLE_SEAT", (plane_id,))
    conn.commit()


def show_flight_infor(cursor, flight_id):
    cursor.execute("SELECT * FROM FLIGHT "
                   "WHERE FLIGHTID=%s", (flight_id,))
    flights = cursor.fetchall()
    if not flights:
        print("No flight information in database")
    else:
        for flight in flights:
            print(flight)


def delete_flight_infor(conn, cursor, flight_id):
    cursor.execute("DELETE FROM FLIGHT WHERE FLIGHTID=%s", (flight_id,))
    conn.commit()


def show_flight_by_date(cursor, origin, des, date):
    cursor.execute("SELECT * FROM FLIGHT "
                   "WHERE ORIGIN=%s AND DESTINATION=%s AND DEPARTURE_DATE=%s", (origin, des, date,))
    flights = cursor.fetchall()
    if not flights:
        print("No Flight")
    else:
        for flight in flights:
            print(flight)


def get_flight_info_by_date(cursor, origin, dest, depart_date, arrival_date):
    cursor.execute("SELECT * FROM FLIGHT "
                   "WHERE ORIGIN=%s AND DESTINATION=%s AND DEPARTURE_DATE=%s AND ARRIVAL_DATE=%s",
                   (origin, dest, depart_date, arrival_date,))
    flights = cursor.fetchall()
    if not flights:
        return None
    else:
        return flights


##################################################

############### PASSENGER SECTION ################

def insert_passenger_info(conn, cursor, passid, passname, passphonenumber, passaddress, passidno):
    cursor.execute("INSERT INTO PASSENGER VALUES(%s, %s, %s, %s, %s)",
                   (passid, passname, passphonenumber, passaddress, passidno,))
    conn.commit()


def show_passenger_info_by_id(cursor, passid):
    cursor.execute("SELECT * FROM PASSENGER "
                   "WHERE PASSID=%s", (passid,))
    passengers = cursor.fetchall()
    if not passengers:
        print("No passenger information in database!")
    else:
        for passenger in passengers:
            print(passenger)


def show_all_passenger_info(cursor):
    cursor.execute("SELECT * FROM PASSENGER")
    passengers = cursor.fetchall()
    if not passengers:
        print("No passenger in database!")
    else:
        for passenger in passengers:
            print(passenger)


def delete_passenger_info(conn, cursor, passid):
    cursor.execute("DELETE FROM PASSENGER WHERE PASSID=%s", (passid,))
    conn.commit()


##################################################

############### EMPLOYEE SECTION #################

def insert_employee_info(conn, cursor, empid, empname, empaddress, empphonenumber, empposition):
    cursor.execute("INSERT INTO EMPLOYEE VALUES(%s, %s, %s, %s, %s)",
                   (empid, empname, empaddress, empphonenumber, empposition,))
    conn.commit()


def show_employee_infor_by_id(cursor, employee_id):
    cursor.execute("SELECT * FROM EMPLOYEE "
                   "WHERE EMPID=%s", (employee_id,))
    employees = cursor.fetchall()
    if not employees:
        print("No employee in database")
    else:
        for employee in employees:
            print(employee)


def show_employee_info(cursor):
    cursor.execute("SELECT * FROM EMPLOYEE")
    employees = cursor.fetchall()
    if not employees:
        print("No employee in database")
    else:
        for employee in employees:
            print(employee)


def update_employee_info(conn, cursor, emp_id, emp_name, emp_add, emp_phonenum, emp_position):
    cursor.execute(
        "UPDATE EMPLOYEE SET EMPNAME=%s, EMPADD=%s, EMPPHONENUM=%s, "
        "EMPPOSITION=%s WHERE EMPID=%s",
        (emp_name, emp_add, emp_phonenum, emp_position, emp_id,))
    conn.commit()


def delete_employee_infor(conn, cursor, emp_id):
    cursor.execute("DELETE FROM EMPLOYEE WHERE EMPID=%s", (emp_id,))
    conn.commit()


# Employees information in Flight (input Flight ID)
def employee_infor_in_flight(cursor, flightid):
    cursor.execute("SELECT EMPID, EMPNAME, EMPADD, EMPPHONENUM, EMPPOSITION "
                   "FROM TICKET T JOIN EMPLOYEE E ON T.EMPID=E.EMPID "
                   "WHERE T.EMPID=%s", (flightid,))
    employees = cursor.fetchall()
    if not employees:
        print("Invalid FLIGHT ID")
    else:
        for employee in employees:
            print(employee)


# Passenger information in Flight (input Flight ID)
def passenger_infor_in_flight(cursor, flightid):
    cursor.execute("SELECT PASSID, PASSNAME, PASSADDRESS, PASSPHONENUMBER, PASSIDNO "
                   "FROM TICKET T JOIN PASSENGER P ON T.EMPID=P.PASSID "
                   "WHERE T.EMPID=%s", (flightid,))
    passengers = cursor.fetchall()
    if not passengers:
        print("Invalid passenger ID")
    else:
        for passenger in passengers:
            print(passenger)


##################################################

################ TICKET SECTION ##################


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
    return chosen_flight_id[-3:] + pas_id[-3:] + pas_name.strip().replace(" ", "")[:3] + str(number_pas) + origin[:2] \
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
    services = 20000  # magic number :v
    tax = int((number_pas * fix_cost_seat_type1 + dist(origin, destination) * fuel_cost + services) * 10 / 100)

    if seat_type == 1:
        total = number_pas * fix_cost_seat_type1 + dist(origin, destination) * fuel_cost + services + tax
    elif seat_type == 2:
        total = number_pas * fix_cost_seat_type2 + dist(origin, destination) * fuel_cost + services + tax
    if round_trip:
        return total*2
    return total


def create_ticket(cursor, pas_id, pas_name, number_pas, origin, destination, depart_date, return_date,
                  round_trip, seat_type):
    # Check available flight
    # If exist
    flights = get_flight_info_by_date(cursor, origin, destination, depart_date, return_date)
    if not flights:
        print("[ERROR 101]! DID NOT FIND ANY FLIGHT MATCH! TRY AGAIN")
    else:
        # Check available seat
        print("CHOOSE AVAILABLE FLIGHTS FOR MORE DETAIL")
        print(flights)
        chosen_flight_id = input("PLEASE PROVIDE THE FLIGHT ID YOU WANT TO BOOK: ")
        chosen_flight = [flight for flight in flights if chosen_flight_id == flight[0]]
        # If yes
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
                total_cost = get_ticket_price(seat_type, number_pas, origin, destination, depart_date, return_date,
                                              round_trip)

                cur.execute("INSERT INTO TICKET(TICKETID, PASSID, FLIGHTID, SEATTYPE, TOTALCOST) "
                               "VALUES (%s, %s, %s, %s, %s)",
                               (ticket_id, pas_id, chosen_flight_id, seat_type, total_cost,))
                if seat_type == 1:
                    cur.execute("UPDATE FLIGHT SET QUANTITY_SEAT1=%s WHERE FLIGHTID=%s",
                                   (available_seats[0]-number_pas, chosen_flight_id))
                elif seat_type == 2:
                    cur.execute("UPDATE FLIGHT SET QUANTITY_SEAT2=%s WHERE FLIGHTID=%s",
                                   (available_seats[1] - number_pas, chosen_flight_id))
                conn.commit()
                print("YOUR TICKET IS CREATED SUCCESSFULLY!")
            except mysql.connector.Error as error:
                print(f"[ERROR {error}]! FAILED TO UPDATE RECORD TO DATABASE. ROLLING BACK... ")
                conn.rollback()
        else:
            print(
                f"[ERROR 102]! OUT OF SEAT, AVAILABLE SEAT {available_seats[seat_type - 1]} BUT YOU NEED {number_pas} "
                f".TRY ANOTHER TYPE OF SEAT OR FLIGHT. THANKS! ")


##################################################


############### EXECUTION SECTION ################
'''
if __name__ == "__main__":
    ############### CONNECTION SECTION ################
    try:
        connect = mysql.connector.connect(
            user="root",
            password="FzrTscd0aGODkVIUXtsa",
            host="containers-us-west-44.railway.app",
            port=5960,
            database="railway"
        )

        cur = connect.cursor()
    except mysql.connector.Error as e:
        print(f"Error connecting to Mysql Platform: {e}")
        connect.rollback()
        sys.exit(1)
    ##################################################

    # ******* TEST YOUR CODE HERE ******** #

    ########################################

##################################################
'''