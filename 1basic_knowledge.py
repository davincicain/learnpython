# #This is a python program.
# from site import setquit
# from tokenize import triple_quoted
#
# print("hello world1")#This is also a python program.
#
# #ctrl+？: This is a multi-line quick comment.
# # print("hello world2")
# # print("hello world3")
# # print("hello world4")
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
# #float: floating-point/decimal
# c=3.14
# print(c)
# d=4.5
# print(d)
# e=6.0
# print(e)
# f=0.0
# print(f)
# print(c+d+e+f)
#
# #Values of numeric types can participate in calculations.
# print(a+b/2+c*7+d+e+f)
#
# #Floating-point values will introduce errors when participating in operations.
# print(9.6/3)
#
# #str: string
# g="hello world5"
# print(g)
# h='hello world6'
# print(h)
# i=""
# print(i)
# j=" "
# print(j)
# k="7"
# print(k)
# l="8.90"
# print(l)
# m="_"
# print(m)
# print(g,h,i,j,k,l,m)
#
# #String types can not be calculated, they can only be concatenated.
# print(k+j+g+i+h+m+l)
#
# #bool: boolean, Boolean type only has two values: True or False
# n=True#T should be capitalized
# o=False#F should be capitalized
# print(n)
# print(o)
# print(k>l)
# print(k<l)
#
# #None, None is a special null value, not zero.
# p=None#N should be capitalized
# print(p)
# print("null value:",p)
#
# #sting concatenation
# q="zhangsan"
# r="lisi"
# print(q+r)#The plus sign concatenates the stings, so no spaces are displayed.
# print(q,r)#The comma does not concatenate the strings, it simply prints the variable contents consecutively, resulting in spaces in display.
# s=q+r
# print(s)
# t=q+" love "+r
# print(t)
#
# #format, Use the format function to concatenate.
# u="hello {}".format("world!")
# print(u)
# v="hello {}, {}, {}".format("world!",q,r)
# print(v)
# w="hello {0}, {1}, {2}".format("world!",q,r)
# print(w)
# x="hello {x}, {b}, {c}".format(x="world!",b=q,c=r)
# print(x)
#
# #escape characters
# y="This is the first line! This is the second line!"
# print(y)
# z="This is the first line!\n\n\nThis is the second line!"#\n: newline character
# print(z)
# a1="Who are you?\t\t\tStay away from me!"#\t: tab,approximately four spaces
# print(a1)
#
# #cancel escape, Commonly used for URLs and file path.
# b1=r"D:\py\PythonProject1\name\test.py"
# print(b1)
# c1="D:\\py\\PythonProject1\\name\\note1.py"
# print(c1)
#
# #get data type
# d1="123"
# print(type(d1))
# e1=456
# print(type(e1))
#
# # data type conversion
# f1="789"
# g1=int(f1)#convert to integer tpye.
# print(type(g1))
# print(g1+1)
#
# h1=2.34
# i1=int(h1)
# print(type(i1))
# print(i1+5)
#
# j1="6.78"
# k1=float(j1)#convert to floating point type.
# print(type(k1))
# print(k1+9)
#
# l1=1
# m1=float(l1)
# print(type(m1))
# print(m1)
# print(m1+2)
#
# n1=345
# o1=str(n1)#convert to string type.
# print(type(o1))
# print(n1)
#
# p1=True
# q1=str(p1)
# print(type(q1))
# print(q1)
#
# #convert to boolean type
# #Values representing zaro or empty will be converted to false.
# r1=0
# print(bool(r1))
# s1=0.0
# print(bool(s1))
# t1=""
# print(bool(t1))
#
# #Other Values will be converted to true.
# u1=1
# print(bool(u1))
# v1=6
# print(bool(v1))
# w1=7.8
# print(bool(w1))
# x1="a"
# print(bool(x1))
# y1=" "
# print(bool(y1))
#
# #arithmetic operators: + - * /
# z1=10
# a2=3
# print(z1/a2)
# print(z1//a2)#//: keep only the integer part
# print(z1%a2)#get the remainder
# print(z1**a2)#get the power
#
# #assignment operators: = += -=
# b2=1
# b2+=2#equals b2=b2+2
# print(b2)
#
# #relational operators: > < == >= <= !=
# #The result is boolean type.
# c2=3
# d2=4
# print(c2==d2)
# print(c2==c2)
# print(c2>d2)
# print(c2<d2)
# print(c2>=d2)
# print(c2<=d2)
# print(c2!=d2)
# print(c2!=c2)
#
# e2="hello"
# f2="Hello"
# print(e2==f2)
#
# #logical operators: and or not
# print(5>6 and 5<6)
# print(5>6 or 5<6)
# print(not 5>6)
#
# #container
# #list: orderly, allow repetition, can store multiple data types
# listg2=[1,2.3,"zhangsan","lisi","wangwu","zhaoliu","zhangsan",True,None]
# print(listg2)
#
# print(listg2[2])#Obtaining a single value using an ascending index: 0 1 2 3 ...
# print(listg2[6])
# print(listg2[-7])#Obtaining a single value using a descending index: ... -4 -3 -2 -1
# print(listg2[-3])
#
# #slice: get a portion of the original list
# print(listg2[2:8:2])#[staring index(inclusive),ending index(exclusive),stpe size(default to 1 if not defined)]
# print(listg2[2:])
# print(listg2[:8])
# print(listg2[::2])
#
# #add data from list
# listg2.append("qianqi")#Add data to the end of the list.
# print(listg2)
#
# listg2.insert(4,"sunba")#Add data at the specified position in the list.
# print(listg2)
#
# #delete data from list
# listg2.remove("wangwu")#Delete the specified data from the list.
# print(listg2)
#
# listg2.pop(5)#Delete the data at the specified position in the list.
# print(listg2)
#
# #reassign values to the data in the list
# listg2[6]="zhoujiu"
# print(listg2)
#
# #merge list
# listh2=["wushi","zhengshiyi"]
# listi2=listg2+listh2
# print(listi2)
#
# #tuple: Elements can not be modified.
# tuplej2=(1,2.3,"zhangsan","lisi","wangwu","zhaoliu","zhangsan",True,None)
# print(tuplej2)
# print(tuplej2[1])
# print(tuplej2[-1])
# print(tuplej2[3:7:2])
#
# #multidimensional containers
# listk2=[listg2,"tangsen",[7,8,9,tuplej2],listh2]
# print(listk2)
# print(listk2[2])
# print(listk2[2][3])
# print(listk2[2][3][4])
#
# #dictionary: key-value, keys can not be duplicated, but values can be duplicated, disorder
# dictl2={"m2":"sunwukong","n2":5,"o2":"zhubajie"}
# print(dictl2)
# print(dictl2["m2"])
# print(dictl2["n2"])
# print(dictl2["o2"])
#
# #modify dictionary values
# dictl2["m2"]="sasen"
# print(dictl2["m2"])
#
# #add data to the dictionary
# dictl2["p2"]=6
# print(dictl2)
#
# #delete date from dictionary
# dictl2.pop("n2")
# print(dictl2)
#
# #Determine if a key exists in the dictionary.
# print("n2" in dictl2)
# print("m2" in dictl2)
#
# #set: disorder, no repetition, set is a type of the dictionary without keys
# setq2={7,8,9,0,1,2,3,4,5,6,7,8,9,"bailongma"}
# print(setq2)#display only non-repeating data
#
# #deduplication
# setr2=set(listg2)
# print(setr2)
# lists2=list(setr2)
# print(lists2)
#
# #set operation
# sett2={0,1,2,3,4,5,6,7,8,9,"qiaofeng"}
# print(setq2&sett2)#intersection
# print(setq2|sett2)#union
# print(setq2-sett2)#collection
# print(sett2-setq2)#collection
# print(setq2^sett2)#Symmetrical difference
#
# #get the container length
# print(len(listg2))
# print(len(tuplej2))
# print(len(dictl2))
# print(len(setq2))
#
# #operations of containers, the container must contain only numeric types
# listu2=[5,6,5,4,5,7,5,3,5,8,5,2,5,9,5,1,5,0,5]
# tuplev2=(5,6,5,4,5,7,5,3,5,8,5,2,5,9,5,1,5,0,5)
# setw2={5,6,5,4,5,7,5,3,5,8,5,2,5,9,5,1,5,0,5}
# print(listu2)
# print(tuplev2)
# print(setw2)
#
# print(max(listu2))#Get the maximum element in container.
# print(max(tuplev2))
# print(max(setw2))
#
# print(min(listu2))#Get the minimum element in container.
# print(min(tuplev2))
# print(min(setw2))
#
# print(sum(listu2))#Sum the values within the container.
# print(sum(tuplev2))
# print(sum(setw2))
#
# listu2.sort()#Sort the values in the list in ascending order.
# print(listu2)
# listu2.sort(reverse=True)#Sort the values in the list in descending order.
# print(listu2)
#
# print(listu2.count(5))#Count the number of occurrence of elements in the container.
# print(tuplev2.count(5))
#
# print(listu2.index(6))#Obtaining the index through the value in the container
# print(tuplev2.index(5))
#
# print(dictl2.get("o2"))#Get the value in the dictionary.
# print(dictl2.get("n2"))