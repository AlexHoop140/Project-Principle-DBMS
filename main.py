import mysql.connector
import sys

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


# cur.execute("USES testing")
# cur.execute("CREATE TABLE TEST("
#             "ID NUMBER PRIMARY KEY )")
#
# users = cur.fetchall()
# for x in cur:
#     print(x)


# Insert new plane information
def insert_plane_info(cur, reg_number, plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer):
    cur.execute("INSERT INTO PLANES VALUES(%s, %s, %s, %s, %s, %s)",
                (reg_number, plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer))
    conn.commit()


# Update plane information with registration number
def update_plane_info(cur, reg_number, plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer):
    cur.execute(
        "UPDATE PLANES SET PLANEID=%s, NUMBER_OF_SEAT=%s, QUANTITY_SEAT_TYPE1=%s, QUANTITY_SEAT_TYPE2=%s, "
        "MANUFACTURER=%s WHERE PLANEID=%s",
        (plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer, reg_number,))
    conn.commit()


# Insert planes info
# insert_plane_info(cur, "VN6221", "A321", 207, 16, 191, "AIRBUS")
# insert_plane_info(cur, "VJ305", "A20N", 178, 8, 170, "AIRBUS")
# insert_plane_info(cur, "VN409", "B78X", 207, 16, 191, "BOEING")
# insert_plane_info(cur, "VN248", "B77W", 427, 42, 385, "BOEING")
# insert_plane_info(cur, "VN301", "A359", 305, 63, 242, "AIRBUS")

# Update plane info
# update_plane_info(cur, "VN6221", "A321", 206, 16, 190, "AIRBUS")

def insert_flight_info(cur, flight_id, plane_id, departure_date, arrrival_date, destination, origin, note):
    cur.execute("INSERT INTO FLIGHT(FLIGHTID, PLANEID, DEPARTURE_DATE, ARRIVAL_DATE, DESTINATION, ORIGIN, "
                "NOTE) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                    flight_id, plane_id, departure_date, arrrival_date, destination, origin, note))
    cur.callproc("FILL_AVAILABLE_SEAT", (plane_id,))
    conn.commit()


# Test insert flight info
# insert_flight_info(cur, "T123456", "VJ305", "2022-09-24", "2022-09-24", "SGN", "VCT", "")
# insert_flight_info(cur, "S092911", "VN248", "2022-09-25", "2022-09-25", "SGN", "HAN", "")
# insert_flight_info(cur, "T901292", "VN6221", "2022-10-24", "2022-10-24", "VCT", "DAN", "")
# insert_flight_info(cur, "S129323", "VN409", "2022-12-23", "2022-12-24", "HAN", "LAX", "")


# insert a test plane to test delete function
# insert_flight_info(cur, "K999999", "CK001", "2022-12-23", "2022-12-24", "HAN", "LAX", "")


def delete_plane(cur, plane_id):
    cur.execute("DELETE FROM PLANES "
                "WHERE PLANEID=%s", (plane_id,))
    conn.commit()


# test delete_plane()
# delete_plane(cur,"CK001")

def show_plane_infor(cur, plane_id):
    cur.execute("SELECT * FROM PLANES WHERE PLANEID=%s", (plane_id,))
    myresult = cur.fetchall()
    for x in myresult:
        print(x)


# test show_plane_infor()
# show_plane_infor(cur,"VJ305")

def show_flight_infor(cur, flight_id):
    cur.execute("SELECT * FROM FLIGHT "
                "WHERE FLIGHTID=%s", (flight_id,))
    myresult = cur.fetchall()
    if myresult == 0:
        print("No flight information in database")
    else:
        for x in myresult:
            print(x)


# test show_flight_infor()
# show_flight_infor(cur,"S092911")

def delete_flight_infor(cur, flight_id):
    cur.execute("DELETE FROM FLIGHT WHERE FLIGHTID=%s", (flight_id,))
    conn.commit()


# test delete_flight_infor
# delete_flight_infor(cur, "K999999")

def insert_passenger_info(cur, passid, passname, passphonenumber, passaddress, passidno):
    cur.execute("INSERT INTO PASSENGER VALUES(%s, %s, %s, %s, %s)",
                (passid, passname, passphonenumber, passaddress, passidno,))
    conn.commit()


# Test insert passenger info
# insert_passenger_info(cur, "P000000100", "LE PHUONG TRUNG", "0945933710", "CAN THO", "092202006275")
# insert_passenger_info(cur, "P000000111", "NGU CONG KHANH", "0945933711", "CAN THO", "092202006271")
# insert_passenger_info(cur, "P000000200", "NGUYEN HOANG DANG HUY", "0911911711", "CAN THO", "092202006272")
# insert_passenger_info(cur, "P000000123", "LE TRUNG KIEN", "0922223210", "AN GIANG", "092202006276")
# insert_passenger_info(cur, "P000000124", "NGUYEN HOANG MINH", "0166999770", "VINH LONG", "092202006279")

def show_passenger_info(cur, passid):
    cur.execute("SELECT * FROM PASSENGER "
                "WHERE PASSID=%s", (passid,))
    myresult = cur.fetchall()
    if len(myresult) == 0:
        print("No passenger information in database!")
    else:
        for x in myresult:
            print(x)


# show_passenger_info(cur, "P000000100")

def delete_passenger_info(cur, passid):
    cur.execute("DELETE FROM PASSENGER WHERE PASSID=%s", (passid,))
    conn.commit()

#show all flight in an input date
def show_flight_in_date(cur, origin, des, date):
    cur.execute("SELECT * FROM FLIGHT "
                "WHERE ORIGIN=%s AND DESTINATION=%s AND DEPARTURE_DATE=%s", (origin, des, date,))
    myresult = cur.fetchall()
    if len(myresult)==0:
        print("No Flight")
    else:
        for x in myresult:
            print(x)

#show_flight_in_date(cur, "HAN", "SGN", "2022-09-25")

#Empoyees information in Flight (input Flight ID)
def employeeInfor_in_flight(cur, flightid):
    cur.execute("SELECT EMPID, EMPNAME, EMPADD, EMPPHONENUM, EMPOSITION "
                "FROM TICKET T JOIN EMPLOYEE E ON T.EMPID=E.EMPID "
                "WHERE T.EMPID=%s", (flightid,))
    myresult = cur.fetchall()
    if len(myresult)==0:
        print("Invalid FLIGHT ID")
    else:
        for x in myresult:
            print(x)

#Passenger information in Flight (input Flight ID)
def passengerInfor_in_flight(cur, flightid):
    cur.execute("SELECT PASSID, PASSNAME, PASSADDRESS, EMPPHONENUMBER, PASSIDNO "
                "FROM TICKET T JOIN PASSENGER P ON T.EMPID=P.PASSID "
                "WHERE T.EMPID=%s", (flightid,))
    myresult = cur.fetchall()
    if len(myresult)==0:
        print("Invalid FLIGHT ID")
    else:
        for x in myresult:
            print(x)