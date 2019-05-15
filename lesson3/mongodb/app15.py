# Author: Ali Azhari

# Sort the result by lastname

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

mydoc = mycol.find().sort("lastname")

for x in mydoc:
    print(x)
