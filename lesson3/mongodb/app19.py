# Author: Ali Azhari

# Delete all documents in the "agents" collection:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")