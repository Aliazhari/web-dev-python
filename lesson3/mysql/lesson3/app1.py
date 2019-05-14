# Author: Ali Azhari

# Delete with %s to prevent the SQL injection

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="chat_db"
)

mycursor = mydb.cursor()

sql = "DELETE FROM agents WHERE name = %s"
name = ("MaRiAa", )

mycursor.execute(sql, name)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")