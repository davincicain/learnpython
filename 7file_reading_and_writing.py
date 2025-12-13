"""
IO: input stream and output stream
RAM: random access memory: store temporary files
hard disk: file: store permanent files
read files: read the file from the disk into the memery
write files: write the file from the memery to the desk
"""
# #"r": file reading
# file=open(r"D:\shaojun3\Desktop\py\reference\poem.txt","r",encoding="utf-8")#open or create a file
# data=file.read()#read the whole file
# print(data)
# file.close()#close the file
#
# file=open(r"D:\shaojun3\Desktop\py\reference\poem.txt","r",encoding="utf-8")
# data=file.readline()#read the file line by line, reading only one line each time
# print(data)
# file.close()
#
# file=open(r"D:\shaojun3\Desktop\py\reference\poem.txt","r",encoding="utf-8")
# data=file.readlines()#read the file line by line and store each line'st content into the list
# print(data)
# file.close()
#
# #the pionter fo the file
# file=open(r"D:\shaojun3\Desktop\py\reference\poem.txt","r",encoding="utf-8")
# data1=file.read()#the pointer reads the file content from beginning to end and stays at the end of the file content
# data2=file.read()#the pointer continues to read the file content from the end, but fails to read anything.
# print(data1)
# print("--------------------")
# print(data2)#printing failed:
# file.close()
#
# file=open(r"D:\shaojun3\Desktop\py\reference\poem.txt","r",encoding="utf-8")
# data1=file.read()
# file.seek(0)#put the pointer to the beginning
# data2=file.read()
# print(data1)
# print("--------------------")
# print(data2)
# file.close()
#
# #"w": file writing
# #writing will empty the existing content first
# #open a existing file or create a new file and write content into it
# #the file path must be correct and the new folder can't be created
# string="hello world"
# file=open(r"D:\shaojun3\Desktop\py\reference\writing.txt","w")
# file.write(string)
# file.close()
#
# #"a": appending and write to the file
# string="hello shanghai"
# file=open(r"D:\shaojun3\Desktop\py\reference\writing.txt","a")
# file.write(string)
# file.close()