from pymongo import MongoClient
mycon=MongoClient("localhost:27017")
mydb=mycon["TCS"]
mycol=mydb["emp"]
rec=mycol.find_one({"name":"Shantunu"})
print(rec)