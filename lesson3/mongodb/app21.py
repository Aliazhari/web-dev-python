# Author: Ali Azhari

# Change the password for Susan:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

myquery = {"name": "Susan"}
newvalues = {"$set": {"password": "1980"}}

mycol.update_one(myquery, newvalues)

# print "agents" after the update:

for x in mycol.find():
    print(x)
