from pymongo import MongoClient
mycon=MongoClient("localhost:27017")
mydb=mycon["TCS"]
mycol=mydb["emp"]
mycol.delete_many({"city":"Gaya"})
