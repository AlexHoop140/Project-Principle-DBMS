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

# Update plane info
# update_plane_info(cur, "VN6221", "A321", 206, 16, 190, "AIRBUS")

