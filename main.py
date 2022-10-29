import mysql.connector

mydb = mysql.connector.connect(
    host = "containers-us-west-44.railway.app",
    user = "root",
    password = "FzrTscd0aGODkVIUXtsa",
    port = 5960,
    database = "railway"
)

mycusor = mydb.cursor()

mycusor.execute("SELECT * FROM sinhvien")
for x in mycusor:
    print(x)