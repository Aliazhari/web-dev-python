# Author: Ali Azhari

# insert a record and print the id of the last record inserted

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="chat_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO agents (lastname, firstname, name, email, password, avail) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("McCarthy", "Joe","Joe", "mJoe@gmail.com", "1234", 0)
mycursor.execute(sql, val)

mydb.commit()


print("Record with id " + mycursor.lastrowid, " was inserted.")