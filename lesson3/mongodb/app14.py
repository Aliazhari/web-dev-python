# Author: Ali Azhari

# filter with regular expression

# Find documents where the address starts with the letter "S":

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

myquery = {"name": {"$regex": "^S"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
