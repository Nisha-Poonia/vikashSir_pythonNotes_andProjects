
# "Python: Starting at 3:12 PM"
# import wikipedia
# results=wikipedia.summary("infosys ltd.", sentences=3)
# print(results)

# #New Program
# import os
# os.startfile("D://cetpa/cetpa.mp4")

# #New Program
# import random
# L1=[22,33,55,77,99]
# print(random.choice(L1))

# # #New Program
# import os
# import random
# # music_dir = 'D:\\OldSongs'  # \\ slash is to escape the character
# songs = os.listdir('D:\\OldSongs')  # listdir is used to enlist all the songs of mentioned directory
# print(songs)
# song=random.choice(songs)
# print(song)
# os.startfile("D://OldSongs//"+song)
# # # os.startfile(os.path.join(music_dir, songs[0]))

"""No Practice No Learning"""

r"""
How to create exe in Python
Install PyInstaller Module
On Command Prompt (CMD) type and enter following command:

pyinstaller --onefile D://cetpa/calci1.py


After execution calci1.exe file will reach in 'C:\Users\HP\dist'
ie in dist folder of the users. """

"""
List Comprehension:
If we want to perform a common operation on all or
selected elements of an iterator and want to generate
a list then we can use list comprehension.


res_list=[element for loop on iterator condition]
Passing condition in list comprehension is optional
"""
# #New Program
# s=r"ce\ntpa"
# print(s)

# #New Program: Square of all elements
# L1=[1,2,3,4,5,6,7,8,9,10]
# L2=[]
# for e in L1:
#     ele=e**2
#     L2.append(ele)
# print(L2)

# #New Program: Square of odd valued elements
# L1=[1,2,3,4,5,6,7,8,9,10]
# L2=[]
# for e in L1:
#     if(e%2==1):
#         ele=e**2
#         L2.append(ele)
# print(L2)


# #New Program: Square of all elements
# L1=[1,2,3,4,5,6,7,8,9,10]
# L2=[e**2 for e in L1]
# print(L2)

# #New Program: Square of odd valued elements
# L1=[1,2,3,4,5,6,7,8,9,10]
# L2=[e**2 for e in L1 if e%2==1]
# print(L2)

# #New Program
# s="12345"
# L1=[int(e) for e in s]
# print(L1)

# #New Program
# s="12345"
# L1=list(s)
# print(L1)

"""How to create your own Iterators
Iterators are objects/variables in Python on which
for loop can be executed

Iterables are data types/classes having __iter__() 
and __next__() method in it.
"""
# L1=[10,20,30]
# for e in L1:
#     print(e)

# #New Program
# L1=[10,20,30]
# iter=L1.__iter__()
# e=iter.__next__()
# print(e)
# e=iter.__next__()
# print(e)
# e=iter.__next__()
# print(e)
# e=iter.__next__()  #StopIteration Error
# print(e)


# #New Program
# for i in range(2,8):
#     print(i)

# #New Program: evenRange(2,8):
# class evenRange:
#     def __init__(self,start,stop):
#         self.start=start
#         self.stop=stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if(self.start>=self.stop):
#             raise StopIteration
#         if(self.start%2==1):
#             self.start+=1       #self.start=4
#         temp=self.start     #temp=4, 6
#         self.start+=2       #self.start=6,8
#         return temp
# for i in evenRange(3,8):
#     print(i)        #i=2,4,6
#
# obj=evenRange(3,8)
# iter=obj.__iter__()
# e=iter.__next__()
# print(e)
# e=iter.__next__()
# print(e)


# #New Program
# for i in range(2,4,0.1): #Error
#     print(i)

#New Program
try:
    # ---bll---layar---
    class CMS:
        cms_id = []

        def _init_(self):
            self.id = 0
            self.name = ""
            self.age = 0
            self.mob = 0
            self.email = ""
            self.address = ""
            self.city = ""
            self.gender = ""

        def add_cms(self):
            # for i in CMS.cms_id:
            try:
                if self not in CMS.cms_id:
                    CMS.cms_id.append(self)

                else:
                    raise NotImplementedError("Id is duplicate ")
            except NotImplementedError as err:
                print("error !", err)


    # --pl--
    def showcustomer(ob):
        print("customer id ", ob.id, "customer name ", ob.name, "customer age ", ob.age, "customer mobile no. ", ob.mob,
              "customer email ", ob.email, "customer address", ob.address, "custome city name ", ob.city,
              "customer Gender", ob.gender)


    print("Welcome to Amazon Customer management system")
    while True:
        ob = CMS()
        choice = input("enter 1 for add customer \n2 for show customer \n3 for exit ")
        if (choice == "1"):
            ob.id = input("Enter Customer Id ")
            ob.name = input("Enter Customer Name ")
            ob.age = input("Enter Customer Age ")
            ob.mob = input("Enter Customer Mobile ")
            ob.email = input("Enter Customer Email ")
            ob.address = input("Enter Customer Address ")
            ob.city = input("Enter Customer City name ")
            ob.gender = input("Enter Customer Gender ")
            ob.add_cms()
            # if(ob.id in CMS.cms_id):
            print("Add Customer Successfully  ")
        elif (choice == "2"):
            for i in CMS.cms_id:
                showcustomer(i)


except NotImplementedError as err:
    print("Error !", err)


except Exception as err:
    print("error !", err)













