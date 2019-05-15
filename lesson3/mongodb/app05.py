# Author: Ali Azhari

# Inserting a record in the collection

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

mydict = { "lastname": "Smith", "firstname": "John","name": "John", "email": "jSmith@xxx.com","password": "1234", "avail": 0 }

x = mycol.insert_one(mydict)