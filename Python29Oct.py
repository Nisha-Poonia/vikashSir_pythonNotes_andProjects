"Python: Database Connectivity"
"""Yesterday we sent select query to database from Python
ie DQL query

Now DML: Data Modification Language
insert, delete, update: Once we execute DML query from
Python to database, then we need to commit the connection.

"""

# print('"CETPA"')

# #New Program
# import pymysql
# mycon=pymysql.connect(host="localhost",user="root",password="root123")
# mycur=mycon.cursor()    #Object of Cursor Class
# mycur.execute("use db1")
# mycur.execute("insert into tb1 values (40,55,'Sonu')")
# mycur.execute("insert into tb1 values (50,51,'Rishabh')")
# mycon.commit()
# mycon.close()

"""String Formatting or Formatted String"""
# #New Program
# a=39
# n="Vikas"
# print("My Name is n and Age is a Years")
# print("My Name is", n, "and Age is", a, "Years")
# print(f"My Name is {n} and Age is {a} Years")
# print("My Name is %s and Age is %d Years"%(n,a))
# print("My Name is {} and Age is {} Years".format(n,a))
# print("My Name is {name} and Age is {age} Years".format(age=a,name=n))



# #New Program
# import pymysql
# id=input("Enter Customer Id:")
# a=input("Enter Customer Age:")
# n=input("Enter Customer Name:")
# mycon=pymysql.connect(host="localhost",user="root",password="root123")
# mycur=mycon.cursor()    #Object of Cursor Class
# mycur.execute("use db1")
# # print(f"insert into tb1 values({id},{a},{n})")
# mycur.execute(f"insert into tb1 values({id},{a},'{n}')")
# mycon.commit()
# mycon.close()







# #New Program
# import pymysql
# mycon=pymysql.connect(host="localhost",user="root",password="root123")
# mycur=mycon.cursor()    #Object of Cursor Class
# mycur.execute("use db1")
# mycur.execute("delete from tb1 where id=60")
# mycon.commit()
# mycon.close()

#New Program: Dedicate to Pawan
# class C1:
#     def showData1(self):    #Instance Method
#         print("CETPA")
#     @staticmethod
#     def showData2():        #Static Method
#         print("Hello")
#     @staticmethod
#     def showData3(self):
#         print("Welcome")
# ob=C1()
# ob.showData1()
# C1.showData2()
# C1.showData3(ob)

