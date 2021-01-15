import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="ritatripadvisor"
)

cursor = db.cursor()
sql="insert into members (ID, fullname, firmname, email) values (%s,%s,%s,%s)"

values = (12, "MartynasMakalis", "Vilnius-travelagency", "vilniusta@gmail.com")
values = (13, "RenataButkeviciene", "JourneyAdvisor", "rjourneyadvisor@gmail.com")
values = (14, "MatasJonaitis", "Travelquide-Liepa", "liepatg@yahoo.com")


cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)