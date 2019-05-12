# Author: Ali Azhari

# insert a record and print the number of records inserted. In this case there is only one record

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="chat_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO agents (lastname, firstname, name, email, password, avail) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("Smith", "John","John", "sJohn@gmail.com", "1234", 0)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
print(mycursor.lastrowid, "record inserted.")