import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="trungpro123",
        host="localhost",
        port=3306,
        database="testing"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()
# cur.execute(
#     "CREATE TABLE sinhvien (mssv int, hoten varchar(10))"
#     )
cur.execute(
    "select * from sinhvien"
    )

for mssv, hoten in cur:
    print(f"mssv: {mssv}, hoten: {hoten}")

cur.execute(
    "show databases"
    )
for x in cur:
    print(x)

cur.start_trans