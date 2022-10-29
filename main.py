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

cur.execute("SELECT * FROM sinhvien")
# cur.execute("USES testing")
# cur.execute("CREATE TABLE TEST("
#             "ID NUMBER PRIMARY KEY )")
#
# users = cur.fetchall()
for x in cur:
    print(x)


# Insert new plane information
# def insert_plane_info(cur, reg_number, plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer):
#     cur.execute("INSERT INTO PLANE VALUES(?, ?, ?, ?, ?, ?)",
#                 (reg_number, plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer,))


# Update plane information with registration number
# def update_plane_info(cur, reg_number, plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer):
#     cur.execute(
#         "UPDATE PLANE SET plane_name=?, qty_seat=?, qty_seat1=?, qty_seat2=?, manufacturer=? WHERE reg_number=?",
#         (plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer, reg_number,))
