# Author: Ali Azhari

import pymongo

# Inserting multiple documents

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

myList = [{"lastname": "Williams", "firstname": "Susan", "name": "Susan", "email": "wSusan@gmail.com", "password": "1234", "avail": 0},
      {"lastname": "Clooney", "firstname": "Betty", "name": "Betty", "email": "cBetty@gmail.com", "password": "1234", "avail": 0},
      {"lastname": "Clinton", "firstname": "Sam", "name": "Sam", "email": "cSam@gmail.com", "password": "1234", "avail": 0}

       ]


x = mycol.insert_many(myList)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)