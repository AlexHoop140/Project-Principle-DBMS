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
        "UPDATE PLANES SET PLANE_NAME=%s, NUMBER_OF_SEAT=%s, QUANTITY_SEAT_TYPE1=%s, QUANTITY_SEAT_TYPE2=%s, "
        "MANUFACTURER=%s WHERE REG_NUMBER=%s",
        (plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer, reg_number,))
    conn.commit()


# Insert planes info
# insert_plane_info(cur, "VN6221", "A321", 207, 16, 191, "AIRBUS")
# insert_plane_info(cur, "VJ305", "A20N", 178, 8, 170, "AIRBUS")
# insert_plane_info(cur, "VN409", "B78X", 207, 16, 191, "BOEING")
# insert_plane_info(cur, "VN248", "B77W", 427, 42, 385, "BOEING")
# insert_plane_info(cur, "VN301", "A359", 305, 63, 242, "AIRBUS")
#insert a test plane to test delete function
#insert_plane_info(cur, "CK001", "0", 0, 0, 0, "0")

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
#insert a test plane to test delete function
#insert_flight_info(cur, "K999999", "CK001", "2022-12-23", "2022-12-24", "HAN", "LAX", "")


def delete_plane(cur, plane_id):
    cur.execute("DELETE FROM PLANES "
                "WHERE PLANEID=%s", (plane_id,))
    conn.commit()

#test delete_plane()
#delete_plane(cur,"CK001")

def show_plane_infor(cur, plane_id):
    cur.execute("SELECT * FROM PLANES WHERE PLANEID=%s", (plane_id,))
    myresult = cur.fetchall()
    for x in myresult:
          print(x)
#test show_plane_infor()
#show_plane_infor(cur,"VJ305")

def show_flight_infor(cur, flight_id):
    cur.execute("SELECT * FROM FLIGHT "
                "WHERE FLIGHTID=%s", (flight_id,))
    myresult = cur.fetchall()
    for x in myresult:
        print(x)
#test show_flight_infor()
#show_flight_infor(cur,"S092911")

def delete_flight_infor(cur, flight_id):
    cur.execute("DELETE FROM FLIGHT WHERE FLIGHTID=%s", (flight_id,))
    conn.commit()

#test delete_flight_infor
#delete_flight_infor(cur, "K999999")

