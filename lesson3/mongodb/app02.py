# Author: Ali Azhari

import pymongo

# list databases in your mongodb

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


print(myclient.list_database_names())