from pymongo import MongoClient
mycon=MongoClient("localhost:27017")
mydb=mycon["TCS"]
mycol=mydb["emp"]
eid=input("Enter Employee ID : ")

rec=mycol.delete_one({"_id":eid})
if rec:
    print("One Record Deleted..")
else:
    print("Record not found..")