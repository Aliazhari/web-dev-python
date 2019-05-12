# Author: Ali Azhari

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="school_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)