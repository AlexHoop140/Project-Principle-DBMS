import main as mn
import mysql.connector
import sys
import random

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

##################################################

################# PLANE SECTION ##################

# Insert planes info
# mn.insert_plane_info(cur, "VN6221", "A321", 207, 16, 191, "AIRBUS")
# mn.insert_plane_info(cur, "VJ305", "A20N", 178, 8, 170, "AIRBUS")
# mn.insert_plane_info(cur, "VN409", "B78X", 207, 16, 191, "BOEING")
# mn.insert_plane_info(cur, "VN248", "B77W", 427, 42, 385, "BOEING")
# mn.insert_plane_info(conn, cur, "VN12", "A320", 170, 30, 140, "AIRBUS")

# Update plane info
# mn.update_plane_info(conn, cur, "VN6221", "A321", 206, 16, 190, "AIRBUS")

# insert a test plane to test delete function
# mn.insert_flight_info(conn, cur, "K999999", "CK001", "2022-12-23", "2022-12-24", "HAN", "LAX", "")

# test delete_plane()
# mn.delete_plane(conn, cur, "CK001")

# test show_plane_infor()
#mn.show_plane_infor(cur, "VJ305")

##################################################

################# FLIGHT SECTION #################


# Test insert flight info
# mn.insert_flight_info(conn, cur, "T123456", "VJ305", "2022-09-24", "2022-09-24", "SGN", "VCT", "")
# mn.insert_flight_info(conn, cur, "S092911", "VN248", "2022-09-25", "2022-09-25", "SGN", "HAN", "")
# mn.insert_flight_info(conn, cur, "T901292", "VN6221", "2022-10-24", "2022-10-24", "VCT", "DAN", "")
# mn.insert_flight_info(conn, cur, "S129323", "VN409", "2022-12-23", "2022-12-24", "HAN", "LAX", "")

# test show_flight_infor()
# show_flight_infor(cursor,"S092911")
#mn.show_flight_infor(cur,"S092911")

# test delete_flight_infor
# delete_flight_infor(conn, cursor, "K999999")

# flights = mn.get_flight_info_by_date(cur, "HAN", "SGN", "2022-09-25", "2022-09-25")
# list = [flights[0][7], flights[0][6]]
# print(list[0])
#
# ticket_id = mn.create_ticket_id("S092911", "P000000111", "LE PHUONG TRUNG", 2, "SGN", "HAN")
# print(ticket_id)
#
# shuffle_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# random.shuffle(shuffle_list)
# print(str(shuffle_list[:5]))

#mn.create_ticket(cur, "P000000100", "LE PHUONG TRUNG", 1, "DAD", "VCA", "2022-10-24", "2022-10-24", False, 1)


##################################################

############### PASSENGER SECTION ################

# Test insert passenger info
# insert_passenger_info(conn, cursor, "P000000100", "LE PHUONG TRUNG", "0945933710", "CAN THO", "092202006275")
# insert_passenger_info(conn, cursor, "P000000111", "NGU CONG KHANH", "0945933711", "CAN THO", "092202006271")
# insert_passenger_info(conn, cursor, "P000000200", "NGUYEN HOANG DANG HUY", "0911911711", "CAN THO", "092202006272")
# insert_passenger_info(conn, cursor, "P000000123", "LE TRUNG KIEN", "0922223210", "AN GIANG", "092202006276")
# insert_passenger_info(conn, cursor, "P000000124", "NGUYEN HOANG MINH", "0166999770", "VINH LONG", "092202006279")

# show_passenger_info(cursor, "P000000100")

##################################################

############### EMPLOYEE SECTION #################

# Test insert employee info
# insert_employee_info(conn, cursor, "E00001", "NGUYEN HOANG DANG HUY", "CAN THO", "0832898421", "CABIN CREW")
# insert_employee_info(conn, cursor, "E00002", "LE PHUONG TRUNG", "CAN THO", "0123456789", "PILOT")
# insert_employee_info(conn, cursor, "E00003", "NGU CONG KHANH", "CAN THO", "0987654321", "CABIN CREW")
# insert_employee_info(conn, cursor, "E00004", "LE TRUNG KIEN", "AN GIANG", "0909121212", "CABIN CREW")


# Test show_employee_infor()
# show_employee_infor_by_id(cursor,"E00001")


# Test show employee info
# show_employee_info(cursor)


# Test update_employee_info()
# update_employee_info(conn, cursor, "E00002", "TRIEU GIA HUY", "CAN THO", "0199888777", "PILOT")


# Test delete employee
# delete_employee_infor(conn, cursor,"E00004")


# show_flight_in_date(cursor, "HAN", "SGN", "2022-09-25")

##################################################

################ TICKET SECTION ##################


##################################################
def insert_plane_info_test(conn, cursor, reg_number, plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer):
    cur.execute("INSERT INTO PLANES VALUES(%s, %s, %s, %s, %s, %s)",
                   (reg_number, plane_name, qty_seat, qty_seat1, qty_seat2, manufacturer))
    conn.commit()

insert_plane_info_test(conn, cur,"CK01","CKst","100","50","50", "AIRBUS")