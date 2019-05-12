# Author: Ali Azhari

# Inserting multiple rows and printing the number of rows inserted

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="chat_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO agents (lastname, firstname, name, email, password, avail) VALUES (%s, %s, %s, %s, %s, %s)"
val = [("Williams", "Susan", "Susan", "wSusan@gmail.com", "1234", 0),
        ("Thomas", "Amy", "Amy", "tAmy@gmail.com", "1234", 0),
       ("Clooney", "Betty", "Betty", "cBetty@gmail.com", "1234", 0)
       ]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "were inserted.")