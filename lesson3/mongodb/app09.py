# Author: Ali Azhari

# find all documents in the collection agents

import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = myClient["chat_db"]
myCol = myDB["agents"]

for x in myCol.find():
  print(x)