# Author: Ali Azhari

# find the first document

import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = myClient["chat_db"]
myCol = myDB["agents"]

x = myCol.find_one()

print(x)