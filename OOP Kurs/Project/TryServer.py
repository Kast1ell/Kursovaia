import pyodbc
from datetime import datetime


class Sql:
    def __init__(self, database, server="LAPTOP-L58HMJ8I"):
        self.conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                   "Trusted_Connection=yes;")
        self.query = "-- {}\n\n-- Made in Python".format(datetime.now()
                                                         .strftime("%d/%m/%Y"))


sql = Sql('Database_of_app')
cursor = sql.conn.cursor()
cursor.execute("SELECT * FROM CSGONEWS")
CSGO_N_results = cursor.fetchall()
print(CSGO_N_results)

cursor.execute("SELECT * FROM DotaNEWS")
DOTA_N_results = cursor.fetchall()
print(DOTA_N_results)

cursor.execute("SELECT * FROM Training")
CSGO_T_results = cursor.fetchall()
print(CSGO_T_results)

sql.conn.close()

