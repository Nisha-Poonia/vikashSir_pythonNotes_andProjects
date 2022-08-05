"""Python Continue"""
"""File Handling: To store the data permanently in files
in hard disk. Both storing and retrieving data.
Data Stream. Streaming of data. Streams means a block of
data move from one place to another. 

"""
# f=open("D://cetpa/fil1.txt","w")
# print(type(f))
# f.write("Welcome To CETPA")
# f.close()

"""
open(file path, file mode)

Mode: 2 Categories. 
        COS: Character Oriented Stream
        BOS: Byte Oriented Stream

COS Modes:
w: Write: In write mode, if file does not exist then
            create a file automatically and write from
            starting of file. If file exists then firstly
            truncate the file (delete all its contents)
            and start writing from starting of file.
r: Read: In read mode, if file does not exist then
           error, else read data from starting of file
a: Append: In append mode, if file does not exist then
            create a file automatically and write from
            starting of file. If file exists then will
            write at the end of file.
w+: Write and Read: 
r+: Read and Write
a+: Read and Append    

BOS Modes:
wb: Write Binary: In write mode, if file does not exist then
            create a file automatically and write from
            starting of file. If file exists then firstly
            truncate the file (delete all its contents)
            and start writing from starting of file.
rb: Read Binary: In read mode, if file does not exist then
           error, else read data from starting of file
ab: Append Binary: In append mode, if file does not exist then
            create a file automatically and write from
            starting of file. If file exists then will
            write at the end of file.
wb+: Write and Read Binary: 
rb+: Read and Write Binary
ab+: Read and Append Binary  
"""
# #New Program
# f=open("D://cetpa/file2.txt","r")
# data=f.read()
# print(data)

# #New Program
# f=open("D://cetpa/file1.txt","r")
# data=f.read()
# print(data)
# f.close()

# #New Program
# f=open("D://cetpa/file1.txt","r")
# data=f.read(5)      #No of characters: 5
# print(data)
# f.close()

# #New Program
# f=open("D://cetpa/file2.txt","w")
# data="""Welcome to CETPA
# Award Winning Training Company
# Awarded by Chetan Bhagat, Soha Ali Khan, Shashi Tharoor..
# """
# f.write(data)
# f.close()

# #New Program
# f=open("D://cetpa/file2.txt","w")
# data="""Welcome to CETPA
# Award Winning Training Company
# Awarded by Chetan Bhagat, Soha Ali Khan, Shashi Tharoor..
# """
# f.write(data)
# f.close()

# #New Program
# f=open("D://cetpa/file2.txt","r")
# print(f.tell())
# print(f.read(5))
# print(f.tell())
# print(f.read(4))
# print(f.tell())
# print(f.read(3))
# print(f.tell())
# f.close()

# #New Program
# f=open("D://cetpa/file2.txt","r")
# l1=f.readline()
# print(l1)
# l1=f.readline()
# print(l1)
# f.close()

# #New Program
# f=open("D://cetpa/file3.txt","w")
# f.write("Hello\nWorld\nWelcome to CETPA")
# f.write("Welcome Back\n")
# f.write("CETPA Infotech")
# f.close()

# #New Program
# f=open("D://cetpa/file4.txt","w")
# f.write("abc")
# print()
# f.write("")
# f.write("")
# f.write("CETPA")
# f.close()

# #New Program
# f=open("D://cetpa/file4.txt","w")
# print("Welcome to CETPA. No 1 in Trainings",file=f)
# f.close()

# #New Program
# f=open("D://cetpa/file4.txt","w")

# #New Program
# f=open("D://cetpa/file2.txt","r")
# l1=f.readline()
# print(l1,end="")
# l1=f.readline()
# print(l1,end="")
# f.close()

# #New Program
# f=open("D://cetpa/file3.txt","r")
# data=f.readlines()
# print(data)

# #New Program
# f=open("D://cetpa/file5.txt","w")
# data=555
# f.write(data)   #New Program COS: Data must be in string
# f.close()

# #New Program
# f=open("D:/cetpa/file6.txt","wb")
# data=b"Welcome to CETPA"
# print(type(data))
# f.write(data)
# f.close()


# #New Program
# f=open("D:/cetpa/cetpa.mp4","rb")
# print(f.read(100))
# f.close()

# #New Program
# f1=open("D:/cetpa/cetpa.mp4","rb")
# f2=open("D:/cetpa/cetpa5.mp4","wb")
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()

# #New Program
# f1=open("D:/cetpa/cetpa.mp4","rb")
# f2=open("D:/cetpa/cetpa6.mp4","wb")
# while(1):
#     data=f1.read(1000)
#     if(data==b""):
#         break
#     f2.write(data)
# f1.close()
# f2.close()



# #New Program
# f1=open("D:/cetpa/cetpa.mp4","rb")
# f2=open("D:/cetpa/cetpa7.mp4","wb")
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()

# #New Program
# f1=open("D:/cetpa/cetpa.mp4","rb")
# f2=open("D:/cetpa/cetpa7.mp4","ab")
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()

#New Program
# f=open("D://cetpa/cetpa1.txt","r")

# #New Program
# import time
# while(1):
#     print("CETPA")
#     time.sleep(1)
#     print("Welcome")
#     time.sleep(1)

# #New Program
# import time
# print("*")
# time.sleep(1)
# print("*")
# time.sleep(1)
# print("*")
# time.sleep(1)
# print("*")
# time.sleep(1)
# print("*")
# time.sleep(1)

# #New Program
# import time
# for i in range(5):
#     print("*",end="")
#     time.sleep(1)

#New Program
import time
print("*",end="")
time.sleep(2)
print("*",end="")
time.sleep(2)
print("*",end="")
time.sleep(2)
print("*",end="")
time.sleep(2)
print("*",end="")
time.sleep(2)











