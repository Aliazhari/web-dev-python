# Author: Ali Azhari

# Inserting a record in the collection and returnig  the _id Field

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

mydict = { "lastname": "Kennedy", "firstname": "Peter","name": "Peter", "email": "pKennedy@xxx.com","password": "1234", "avail": 0 }

x = mycol.insert_one(mydict)

print(x.inserted_id)