"Python Continue: File Handling"
# #New Program
# import time
# for i in range(5):
#     print("*")
#     time.sleep(1)

# #New Program
# print("CETPA")
# print("Hello World")

# #New Program
# import time
# for i in range(5):
#     print("*",end="")
#     time.sleep(1)


# #New Program
# import time
# for i in range(5):
#     print("*",end="",flush=True)
#     time.sleep(1)

# #New Program
# f=open("D:/cetpa/file8.txt","w")
# f.write("CETPA")
# f.flush()
# f.close()

"""
No Negative Marking in our Class.

Data Sharing:
Data Transmit/Receive:
Serialization/Deserialization:

Serialization: Conversion of local data/objects to 
some standard format.

Deserialization: Conversion of standard data to local
data/objects

Standard Format for Data Exchange: 
World's most popular format for data exchange is: json
For cross platform/language: json
JSON: Java Script Object Notation: 
Java Script

Python to Python Data Exchange: pickling
Python Objects to Python Object.

"""
# import pickle
# f1=open("D://cetpa/file9.txt","wb")
# L1=["Shyam","Vikas","Anil","Anurag"]
# pickle.dump(L1,f1)
# f1.close()

# #New Program
# import pickle
# f1=open("D://cetpa/file9.txt","rb")
# L1=pickle.load(f1)
# print(L1)
# f1.close()


"""JSON
JSON Customer Object:
[{"id":"10","name":"Vikas","age":"39","mob":"1234"},
 {"id":"20","name":"Anil","age":"41","mob":"2345"},
 .
 .
]



"""
# import json
# f=open("D:/cetpa/fil10.txt","w")
# data=["Welcome",555,99.85]
# json.dump(data,f)
# f.close()

# #New Program
# import json
# class Customer:
#     cuslist=[]
#     def __init__(self,id,name,age,mob):
#         self.id=id
#         self.name=name
#         self.age=age
#         self.mob=mob
# cus=Customer(10,"vikas",39,1234)
# Customer.cuslist.append(cus)
# cus=Customer(20,"Anil",41,2345)
# Customer.cuslist.append(cus)
# print(len(Customer.cuslist))
# print(Customer.cuslist)
# f=open("D:/cetpa/file11.txt","w")
# json.dump(Customer.cuslist,f)
# # print(type(Customer.cuslist[0]))
# f.close()

"""


"""
#New Program
import json
class Customer:
    cuslist=[]
    def __init__(self,id,name,age,mob):
        self.id=id
        self.name=name
        self.age=age
        self.mob=mob
    @staticmethod
    def convtoDict(ob):
        return ob.__dict__
cus=Customer(10,"vikas",39,1234)
Customer.cuslist.append(cus)
cus=Customer(20,"Anil",41,2345)
Customer.cuslist.append(cus)
print(len(Customer.cuslist))
print(Customer.cuslist)
f=open("D:/cetpa/file11.txt","w")
json.dump(Customer.cuslist,f,default=Customer.convtoDict)
# print(type(Customer.cuslist[0]))
print(Customer.cuslist[0].__dict__)
print(cus.__dict__)
f.close()






