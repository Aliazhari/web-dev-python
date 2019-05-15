# Author: Ali Azhari

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["chat_db"]

print(myclient.list_database_names())