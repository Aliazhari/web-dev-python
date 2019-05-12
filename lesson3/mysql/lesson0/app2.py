# Author: Ali Azhari

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE chat_db")