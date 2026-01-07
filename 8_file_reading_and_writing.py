"""
IO: input stream and output stream
RAM: random access memory: store temporary files
hard disk: file: store permanent files
read files: read the file from the disk into the memery
write files: write the file from the memery to the desk
"""
#"r": file reading
#file encoding: gbk/utf-8/gb2312/utf16
file1=open(r"D:\shaojun3\Desktop\py\reference1\poem1.txt","r",encoding="utf-8")#open or create a file
data1=file1.read()#read the whole file
print(data1)
file1.close()#close the file

file1=open(r"D:\shaojun3\Desktop\py\reference1\poem1.txt","r",encoding="utf-8")
data1=file1.readline()#read the file line by line, reading only one line each time
print(data1)
file1.close()

file1=open(r"D:\shaojun3\Desktop\py\reference1\poem1.txt","r",encoding="utf-8")
data1=file1.readlines()#read the file line by line and store each line'st content into the list
print(data1)
file1.close()

#the pionter fo the file
file1=open(r"D:\shaojun3\Desktop\py\reference1\poem1.txt","r",encoding="utf-8")
data1=file1.read()#the pointer reads the file content from beginning to end and stays at the end of the file content
data2=file1.read()#the pointer continues to read the file content from the end, but fails to read anything.
print(data1)
print("--------------------")
print(data2)#printing failed:
file1.close()

file1=open(r"D:\shaojun3\Desktop\py\reference1\poem1.txt","r",encoding="utf-8")
data1=file1.read()
file1.seek(0)#put the pointer to the beginning
data2=file1.read()
print(data1)
print("--------------------")
print(data2)
file1.close()

#"w": file writing
#writing will empty the existing content first
#open a existing file or create a new file and write content into it
#the file path must be correct and the new folder can't be created
string="hello world"
file1=open(r"D:\shaojun3\Desktop\py\reference1\writing1.txt","w")
file1.write(string)
file1.close()

#"a": appending and write to the file
string="hello shanghai"
file1=open(r"D:\shaojun3\Desktop\py\reference1\writing1.txt","a")
file1.write(string)
file1.close()

#"rb"/"wb"/"ab": read and write binary files
file1=open(r"D:\shaojun3\Desktop\py\reference1\whitecat1.jpg", "rb")
data1=file1.read()
file1.close()
print(data1)

file2=open(r"D:\shaojun3\Desktop\py\reference1\whitecat2.jpg", "wb")
file2.write(data1)
file2.close()

file3=open(r"D:\shaojun3\Desktop\py\reference1\whitecat2.jpg", "ab")
file3.write(data1)
file3.close()

#relative path:
# ".": in the current directory
file1=open(r".\reference1\poem1.txt","r",encoding="utf-8")
data1=file1.read()
file1.close()
print(data1)

#"..": the parent directory
file1=open(r"..\..\reference1\poem1.txt","r",encoding="utf-8")
data1=file1.read()
file1.close()
print(data1)

# with-open: close files automatically
with open(r".\reference1\poem1.txt","r",encoding="utf-8") as file:
    data1=file1.read()
print(data1)

#operate read and write simultaneously
with open(r".\reference1\poem1.txt","r",encoding="utf-8") as file1,open(r".\reference1\poem2.txt","w") as file2:
    data1=file1.read()
    file2.write(data1)