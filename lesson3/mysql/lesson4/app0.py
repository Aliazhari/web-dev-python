# Author: Ali Azhari

# Update a row

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="chat_db"
)

mycursor = mydb.cursor()

sql = "UPDATE agents SET password = '1981' WHERE id = '24'"

# or without single quotation

# sql = "UPDATE agents SET password = 1981 WHERE id = 24"


mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")