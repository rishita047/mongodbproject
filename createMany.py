from pymongo import MongoClient
mycon=MongoClient("localhost:27017")
mydb=mycon["TCS"]
mycol=mydb["emp"]
rec=list()
nor=int(input("Enter no of document you have to insert : "))
for i in range(nor):
    eid=input("Enter Employee Id : ")
    name=input("Enter Name of Employee : ")
    phone=input("Enter Phone no of Employee : ")
    age=input("Enter Age of Employee : ")
    city=input("Enter City of Employee : ")
    dict={"_id":eid,"name":name,"phone":phone,"age":age,"city":city}
    rec.append(dict)

result=mycol.insert_many(rec)
if result:
    print("Multiple record inserted successfully.")
else:
    print("Unable to insert records.")
