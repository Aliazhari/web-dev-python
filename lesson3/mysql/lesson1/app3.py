# Author: Ali Azhari

# limit

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="chat_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM agents LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)