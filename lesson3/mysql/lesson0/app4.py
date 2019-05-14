# Author: Ali Azhari

# Drop a table

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="chat_db"
)

mycursor = mydb.cursor()

sql = "DROP TABLE dump"

mycursor.execute(sql)

print("Tabe dump is deleted")