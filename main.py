import mysql.connector
import sys


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


##################################################


############### EXECUTION SECTION ################

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
