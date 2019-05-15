# Author: Ali Azhari

# Find documents where the address starts with the letter "S" or higher:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

myquery = {"name": {"$gt": "S"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
