# Author: Ali Azhari

# Update a row using %s to prevent SQL injection

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="chat_db"
)

mycursor = mydb.cursor()

sql = "UPDATE agents SET password = %s WHERE id = %s"
val = ("2000", "24")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
