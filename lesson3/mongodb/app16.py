# Author: Ali Azhari

# Use the value -1 as the second parameter to sort descending.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

mydoc = mycol.find().sort("lastname", -1)

for x in mydoc:
  print(x)