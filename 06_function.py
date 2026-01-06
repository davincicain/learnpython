# #built-in function
# #absolute value
# a=-1
# print(abs(a))
#
# # aounding
# a=1.2
# print(round(a))
# a=12.3
# b=3
# print(a/b)
# print(round(a/b))
#
# #power
# print(pow(10,3))
#
# #quotient and remainder
# print(divmod(10,3))
#
# #string splitting
# a="yi,er,san,si"
# b=a.split(",")
# print(b)
#
# #string replace
# f="yi,er,san,si"
# f=f.replace("er","wu")
# print(f)
#
# #user-defined function
# #defined function
# def function1():
#     print("function1 has been executed!")
# def function2():
#     function1()#Call a function within a function.
#     print("function2 has been executed!")
#
# for i in range(10):
#     print(i)
#     function1()#function call
# function2()
#
# #function with arguments
# def getSum(a,b):#formal argument
#     c=a+b
#     print(c)
# getSum(1,2)#actual argument, the number of actual parameters and formal parameters needs to be consistent.
#
# def getSum(a,b):#formal parameter
#     c=a+b
#     return c #return value, put at the end of the function.
#
# d=getSum(1,2)/2
# print(d/2)
#
# print(getSum(1,2)/2)
#
# def func1():
#     a=1
#     b=2
#     c=3
#     return a,b,c
# print(func1())#Multiple parameters will be returned in the form of a tuple.
# print(type(func1()))
#
# def func1():
#     print("func3 has been executed!")
#     return#Using a single return is to end the total function.
# func1()
#
# #four ways of passing parameters
# #positional argument
# def func1(nameA,nameB):
#     print(f"{nameA} owes {nameB} one thousand yuan.")
# func1("yi","er")
#
# #keyword argument
# def func1(nameA,nameB):
#     print(f"{nameA} owes {nameB} one thousand yuan.")
# func1(nameA="yi",nameB="er")
#
# #default argument
# def func1(nameA="yi",nameB="er"):
#     print(f"{nameA} owes {nameB} one thousand yuan.")
# func1()
# func1("san")
# func1(nameA="si")
# func1(nameB="wu")
# func1("liu","qi")
# func1("ba",nameB="jiu")
#
# #variable length argument
# def func1(*names):
#     print(f"My friend's name are: ")
#     print(names,type(names))#The output is tuple.
# func1()
# func1("yi","er","san","si")
#
# #The scope of variables
# #Local variable
# def func1():
#     a="yi"
#     print(a)
# print(a)#Reading a variable inside a function outside the function will result in an error.
#
# #Global variable
# a="yi"#Global variable
# def func1():
#    a="er"
#    print(a)#Create a local variable with the same name.
# func1()#Executed the local variable within the function.
#
# a="yi"
# def func1():
#     global a #Declare "a" as a global variable.
#     a="er"
#     print(a)
# func1()
#
# #nested scope
# def function1():
#     a="yi"
#     b="er"
#     c="san"
#     print("f1 has been executed!")
#     print(a)
#     print(b)
#     print(c)
#     def function2():
#         a="si"
#         print("The F2 in F1 has been executed!")
#         print(a)
#         print(b)
#         print(c)
#         def function3():
#             a="wu"
#             b="liu"
#             print("The F3 in F2 has been executed!")
#             print(a)
#             print(b)
#             print(c)
#         function3()
#     function2()
# function1()
#
# #Anonymous function: used for simple calculation
# func1=lambda a,b:a+b
# result=func1(1,2)
# print(result)
#
# #use a function as an argument
# listA=[1,2,3,4,5,6,7,8,9,0]
# listB=filter(lambda x:x%2==0,listA) #Filter all the even numbers from the list
# print(list(listB))
#
# #Decorator
# def decorator(func): #Receive a function as an argument.
#     def wrapper():
#         print("start calling the function!")
#         func()
#         print("The function call has ended!")
#     return wrapper
#
# @decorator #Annotation, add some other functions to the function.
# def sayhello():
#     print("hello world!")
# sayhello()
#
# def d(a):
#     def b():
#         inn=input("please input your password:")
#         if inn == "123456":
#             print("verification was successful!")
#             a()
#         else:
#             print("verification was not successful!")
#     return b
#
# @d
# def c():
#     print("in the process of transfer money!")
# c()