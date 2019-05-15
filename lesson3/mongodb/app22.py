# Author: Ali Azhari

# Update passwords for everyone whose name starts with S to 2019

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

myquery = { "name": { "$regex": "^S" } }
newvalues = { "$set": { "password": "2019" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")