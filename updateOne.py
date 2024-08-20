from pymongo import MongoClient
mycon=MongoClient("localhost:27017")
mydb=mycon["TCS"]
mycol=mydb["emp"]
mycol.update_one({"name":"rishita"},{"$set":{"city":"delhi"}})
print("Record Updated!!!")                               