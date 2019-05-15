# Author: Ali Azhari

# returns some fields
# You are not allowed to specify both 0 and 1 values in the same object
# (except if one of the fields is the _id field).
# If you specify a field with the value 0, all other fields get the value 1, and vice versa:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

for x in mycol.find({},{ "_id": 0, "lastname": 1, "firstname": 1 }):
  print(x)