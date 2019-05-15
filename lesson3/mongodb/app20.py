# Author: Ali Azhari

# drop the whole collection (same as dropping table in mysql)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

mycol.drop()