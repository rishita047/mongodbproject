from pymongo import MongoClient
mycon=MongoClient("localhost:27017")
mydb=mycon["TCS"]
mycol=mydb["emp"]
mycol.update_many({},{"$set":{"company":"TCS"}})
print("All Records Updated!!!")