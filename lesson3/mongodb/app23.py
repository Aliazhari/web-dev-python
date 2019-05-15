# Author: Ali Azhari

# Limit the result to only return 3 documents:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

myresult = mycol.find().limit(3)

# print the result:

for x in myresult:
  print(x)