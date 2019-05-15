# Author: Ali Azhari

import pymongo

# The first argument of the find() method is a query object, and is used to limit the search.

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

myquery = {"name": "Susan"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
