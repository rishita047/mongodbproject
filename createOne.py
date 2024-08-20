from pymongo import MongoClient                         # importing pymongo 
mycon=MongoClient("localhost:27017")                    # connecting with mongodb server
mydb=mycon['TCS']                                       # creating a new database in mongodb using python
mycol=mydb['emp']                                       # creating a collection in tcs database using python
def insertRec():                                        # define a function
    eid=input("Enter Employee ID : ")                   # taking input from user at run time
    name=input("Enter Nmae of Employee : ")
    phone=input("Enter PhoneNo of Employee : ")
    email=input("Enter Email of the Employee : ")
    age = int(input("Enter Age of the Employee : "))
    city=input("Enter City of the Employee : ")
    mycol.insert_one(                                   # inserting one document in the collection
        {
            "_id":eid,
            "name":name,
            "phone":phone,
            "email":email,
            "age":age,
            "city":city
        }
    )
    print("One Record Inserted!!!!")
insertRec()                                             # calling insert function.
insertRec()