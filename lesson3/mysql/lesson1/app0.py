# Author: Ali Azhari

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="chat_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM agents")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)