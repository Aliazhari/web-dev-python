# Author: Ali Azhari

# Delete the document with the name "Sam". Only the first match gets deleted
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chat_db"]
mycol = mydb["agents"]

myquery = {"name": "Sam"}

mycol.delete_one(myquery)
