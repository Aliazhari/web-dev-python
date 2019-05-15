# Author: Ali Azhari

import pymongo

# This example will exclude "password" from the result

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

for x in mycol.find({},{ "password": 0 }):
  print(x)