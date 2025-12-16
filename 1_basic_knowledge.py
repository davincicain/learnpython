# #This is a python comment.
# print("hello world")#This is also a python program.
#
# #ctrl+？: This is a multi-line quick comment.
# # print("hello world1")
# # print("hello world2")
# # print("hello world3")
#
# '''
# this is also a multi-line quick comment.
# this is also a multi-line quick comment.
# this is also a multi-line quick comment.
# '''
#
# """
# this is also a multi-line quick comment.
# this is also a multi-line quick comment.
# this is also a multi-line quick comment.
# """
#
# #int: integer
# a=1
# print(a)
# b=2
# print(b)
# print(a+b)
#
# #float: floating-point
# c=3.45
# print(c)
# d=6.7
# print(d)
# e=8.0
# print(e)
# f=0.0
# print(f)
# print(c+d+e+f)
#
# #Values of numeric types can participate in calculations.
# print(a+b/2+c*3+d+e+f)
#
# #Floating-point values will introduce errors when participating in operations.
# print(9.6/3)
#
# #str: string
# a="hello world1"
# print(a)
# b='hello world2'
# print(b)
# c=""
# print(c)
# d=" "
# print(d)
# e="1"
# print(e)
# f="2.30"
# print(f)
# g="_"
# print(g)
# print(a,b,c,d,e,f,g)#there are spaces between the output values
#
# #String types can not be calculated, they can only be concatenated
# print(a+b+c+d+e+f+g)#there are no space between the output values
#
# #bool: boolean type only has two values: True or False
# a=True#T should be capitalized
# b=False#F should be capitalized
# c=1
# d=0
# print(a)
# print(b)
# print(c>d)
# print(d<c)
# print(1>0)
# print(0>1)
#
# #None: None is a special null value, not zero.
# a=None#N should be capitalized
# print(a)
# print("null value:",a)
#
# #string concatenation
# a="yi"
# b="er"
# print(a+b)#The plus sign concatenates the strings, so no spaces are displayed.
# print(a,b)#The comma does not concatenate the strings, it simply prints the variable contents consecutively, resulting in spaces in display.
# c=a+b
# print(c)
# d=a+" love "+b
# print(d)
#
# #format: Use the format function to concatenate.
# a="你好"
# b="世界"
# c="hello {}".format("world")
# print(c)
# d="hello {}, {} {}".format("world",a,b)
# print(d)
# e="hello {0}, {1} {2}".format("world",a,b)
# print(e)
# f="hello {g}, {h} {i}".format(g="world",h=a,i=b)
# print(f)
#
# #escape characters
# a="This is the first line! This is the second line!"
# print(a)
# b="This is the first line!\n\n\nThis is the second line!"#\n: newline character
# print(b)
# c="Who are you?\t\t\tStay away from me!"#\t: tab,approximately four spaces
# print(c)
#
# #cancel escape, Commonly used for URLs and file path.
# a=r"D:\py\PythonProject1\name\test.py"
# print(a)
# b="D:\\py\\PythonProject1\\name\\note1.py"
# print(b)
#
# #get data type
# a="123"
# print(type(a))
# b=456
# print(type(b))
#
# # data type conversion
# a="123"
# print(type(a))
# b=int(a)#convert to integer tpye.
# print(type(b))
# print(b+4)
#
# a=1.23
# print(type(a))
# b=int(a)#Converting floating - point numbers to integers will result in the loss of the fractional part.
# print(type(b))
# print(b+4)
#
# a="1.23"
# print(type(a))
# b=float(a)#convert to floating point type.
# print(type(b))
# print(b+4)
#
# a=1
# print(type(a))
# b=float(a)
# print(type(b))
# print(b+2)
#
# a=123
# print(type(a))
# b=str(a)#convert to string type.
# print(type(b))
# print(b)
#
# a=True
# print(type(a))
# b=str(a)
# print(type(b))
# print(b)
#
# #convert to boolean type
# #Values representing zaro or empty will be converted to false.
# a=0
# print(bool(a))
# b=0.0
# print(bool(a))
# c=""
# print(bool(c))
# #Other Values will be converted to true.
# d=1
# print(bool(d))
# e=2.0
# print(bool(e))
# f=3.4
# print(bool(f))
# g="a"
# print(bool(g))
# h=" "
# print(bool(h))
#
# #arithmetic operators: + - * /
# a=10
# b=3
# print(a/b)
# print(a//b)#//: keep only the integer part
# print(a%b)#get the remainder
# print(a**b)#get the power
#
# #assignment operators: = += -=
# a=1
# a+=2#equals a=a+2
# print(a)
#
# #relational operators: > < == >= <= !=
# #The result is boolean type.
# a=1
# b=2
# print(a==b)
# print(a==a)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
# print(a!=b)
# print(a!=b)
#
# a="hello"
# b="Hello"
# print(a==b)
#
# #logical operators: and or not
# print(1>2 and 1<2)
# print(1>2 or 1<2)
# print(not 1>2)
#
# #container
# #list: orderly, allow repetition, can store multiple data types
# lista=[1,2.3,"yi","er","san","si","wu",True,None]
# print(lista)
# print(lista[2])#Obtaining a single value using an ascending index: 0 1 2 3 ...
# print(lista[-7])#Obtaining a single value using a descending index: ... -4 -3 -2 -1
#
# #slice: get a portion of the original list
# print(lista[2:8:2])#(staring index(inclusive),ending index(exclusive),stpe size(default to 1 if not defined))
# print(lista[2:])
# print(lista[:8])
# print(lista[::2])
#
# #add data from list
# lista.append("liu")#Add data to the end of the list.
# print(lista)
#
# lista.insert(4,"qi")#Add data at the specified position in the list.
# print(lista)
#
# #delete data from list
# lista.remove("yi")#Delete the specified data from the list.
# print(lista)
#
# lista.pop(5)#Delete the data at the specified position in the list.
# print(lista)
#
# #reassign values to the data in the list
# lista[6]="ba"
# print(lista)
#
# #merge list
# listb=["jiu","shi"]
# listc=lista+listb
# print(listc)
#
# #tuple: Elements can not be modified.
# tuplea=(4,5.6,"shiyi","shier","shisan","shisi","shiwu",True,None)
# print(tuplea)
# print(tuplea[1])
# print(tuplea[-1])
# print(tuplea[3:7:2])
#
# #multidimensional containers
# listc=[lista,"shiliu",[7,8,9,tuplea],listb]
# print(listc)
# print(listc[2])
# print(listc[2][3])
# print(listc[2][3][4])
#
# #dictionary: key-value, keys can not be duplicated, but values can be duplicated, disorder
# dicta={"a":"yi","b":1,"c":True}
# print(dicta)
# print(dicta["a"])
# print(dicta["b"])
# print(dicta["c"])
# print(dicta.get("a"))
# print(dicta.get("b"))
# print(dicta.get("c"))
#
# #modify dictionary values
# dicta["a"]="er"
# print(dicta["a"])
#
# #add data to the dictionary
# dicta["b"]=2
# print(dicta)
#
# #delete date from dictionary
# dicta.pop("c")
# print(dicta)
#
# #Determine if a key exists in the dictionary.
# print("a" in dicta)
# print("b" in dicta)
#
# #set: disorder, no repetition, set is a type of the dictionary without keys
# seta={1,2,2,3,3,3,"yi"}
# print(seta)#display only non-repeating data
#
# #deduplication
# lista=[1,2,2,3,3,3,"yi","er","er","san","san","san"]
# print(lista)
# seta=set(lista)
# print(seta)
# lista=list(seta)
# print(lista)
#
# #set operation
# seta={1,2,2,3,3,3,"yi","er","er","san","san","san"}
# setb={1,2,2,3,3,3,"si","si","si","si"}
# print(seta&setb)#intersection
# print(seta|setb)#union
# print(seta-setb)#collection
# print(setb-seta)#collection
# print(seta^setb)#Symmetrical difference
#
# #get the container length
# lista={0,1,2,3,"ling","yi","er","san"}
# tuplea=(0,1,2,3,"ling","yi","er","san")
# dicta={"a":0,"b":1,"c":"yi"}
# seta={1,2,2,3,3,3,"yi","er","er","san","san","san"}
# print(len(lista))
# print(len(tuplea))
# print(len(dicta))
# print(len(seta))
#
# #operations of containers, the container must contain only numeric types
# lista=[5,6,5,4,5,7,5,3,5,8,5,2,5,9,5,1,5,0,5]
# tuplea=(5,6,5,4,5,7,5,3,5,8,5,2,5,9,5,1,5,0,5)
# seta={5,6,5,4,5,7,5,3,5,8,5,2,5,9,5,1,5,0,5}
# print(lista)
# print(tuplea)
# print(seta)
#
# print(max(lista))#Get the maximum element in container.
# print(max(tuplea))
# print(max(seta))
#
# print(min(lista))#Get the minimum element in container.
# print(min(tuplea))
# print(min(seta))
#
# print(sum(lista))#Sum the values within the container.
# print(sum(tuplea))
# print(sum(seta))
#
# lista.sort()#Sort the values in the list in ascending order.
# print(lista)
# lista.sort(reverse=True)#Sort the values in the list in descending order.
# print(lista)
#
# #Count the number of occurrences of elements in the container.
# lista=[0,1,2,2,3,3,3]
# tuplea=(0,1,2,2,3,3,3)
# print(lista.count(2))
# print(tuplea.count(3))
#
# #Obtaining the index through the value in the container
# print(lista.index(2))
# print(tuplea.index(3))