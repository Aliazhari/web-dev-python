# Author: Ali Azhari

# Importing agents from a CSV file, inserting rows using %s.

import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="ali",
  passwd="ali",
  database="chat_db"
)


def main():
    mycursor = mydb.cursor()
    csv.register_dialect('myAgents', delimiter=',', skipinitialspace=True)
    f = open("agents.csv")
    reader = csv.reader(f, 'myAgents')
    for lname, fname,name, email, passd, avail in reader:
        mycursor.execute("INSERT INTO agents (lastname, firstname, name, email, password, avail) VALUES (%s, %s, %s, "
                         "%s, %s, %s)", (lname, fname, name, email, passd, avail))

        print("Record " + str(mycursor.lastrowid) + " was added")
    mydb.commit()


if __name__ == "__main__":
    main()