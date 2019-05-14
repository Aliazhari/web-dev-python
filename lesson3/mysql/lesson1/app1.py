# Author: Ali Azhari

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="chat_db"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM agents WHERE name = 'peter'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)