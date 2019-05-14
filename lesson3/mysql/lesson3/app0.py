# Author: Ali Azhari

# delete a row

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="chat_db"
)

mycursor = mydb.cursor()

sql = "DELETE FROM agents WHERE name = 'maRiaa'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")