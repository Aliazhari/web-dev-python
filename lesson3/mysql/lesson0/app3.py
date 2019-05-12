# Author: Ali Azhari

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ali",
    passwd="ali",
    database="chat_db"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE agents (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, " \
                 "lastname VARCHAR(20) NOT NULL, firstname VARCHAR(20) NOT NULL, name VARCHAR(20) NOT NULL, " \
                 "email VARCHAR(50) NOT NULL, password VARCHAR(255) NOT NULL, avail SMALLINT NOT NULL)");

mycursor.execute("CREATE TABLE customers (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, " \
                 "name VARCHAR(100) NOT NULL, ip VARCHAR(15) NOT NULL, dt DATETIME NOT NULL, " \
                 "subject VARCHAR(50) NOT NULL)");

mycursor.execute("CREATE TABLE chats (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, " \
                 "agent INT NOT NULL, customer INT NOT NULL, message VARCHAR(255) NOT NULL, ts TIMESTAMP NOT NULL)");
