# #built-in function
# #absolute value
# a=-5
# print(abs(a))
#
# # aounding
# b=3.1415
# print(round(b))
# c=15.3
# d=3
# print(c/d)
# print(round(c/d))
#
# #power
# print(pow(10,3))
#
# #quotient and remainder
# print(divmod(10,3))
#
# #string splitting
# e="zhaoyi,qianer,sunsan,lisi"
# e=e.split(",")
# print(e)
#
# #string replace
# f="zhaoyi,qianer,sunsan,lisi"
# f=f.replace("qianer","zhouwu")
# print(f)
#
# #user-defined function
# #defined function
# def function1():
#     print("function1 has been executed!")
#
# def function2():
#     function1()#Call a function within a function.
#     print("function2 has been executed!")
#
# #function call
# function1()
#
# for i in range(10):
#     print(i)
#     function1()
#
# function2()
#
#function with parameters
#
# def getSum(a,b):#formal parameter
#     c=a+b
#     print(c)
#
# getSum(1,2)#actual parameter, the number of actual parameters and formal parameters needs to be consistent.
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
# def func2():
#     a=1
#     b=2
#     c=3
#     return a,b,c
#
# print(func2())#Multiple parameters will be returned in the form of a tuple.
# print(type(func2()))
#
# def func3():
#     print("func3 has been executed!")
#     return#Using a single return is to end the total function.
#
# func3()

# #four ways of passing parameters
# #positional argument
# def func1(nameA,nameB):
#     print(f"{nameA} owes {nameB} one thousand yuan.")
#
# func1("zhaoyi","qianer")
#
# #keyword argument
# def func2(nameA,nameB):
#     print(f"{nameA} owes {nameB} one thousand yuan.")
#
# func2(nameA="qianer",nameB="zhaoyi")
#
# #default argument
# def func3(nameA="zhaoyi",nameB="qianer"):
#     print(f"{nameA} owes {nameB} one thousand yuan.")
#
# func3()
# func3("sunsan")
# func3(nameA="sunsan")
# func3(nameB="lisi")
# func3("sunsan","lisi")
# func3("sunsan",nameB="lisi")
#
#variable length argument
# def func4(*names):
#     print(f"My friend's name are: ")
#     print(names,type(names))#The output is tuple.
#
# func4()
# func4("zhaoyi","qianer","sunsan","lisi")
#
# #The scope of variables
# #Local variable
# def func():
#     a="zhaoyi"
#     print(a)
# #print(a),Reading a variable inside a function outside the function will result in an error.

# #Global variable
# a="zhaoyi"#Global variable
# def func2():
#    a="qianger"
#    print(a)#Create a local variable with the same name.
#
# func2()#Executed the local variable within the function.
# print(a)#print global variable
#
# a="zhaoyi"
# def func3():
#     global a #Declare "a" as a global variable.
#     a="qianer"
#     print(a)
#
# func3()
#
# #nested scope
# def function3():
#     a="zhaoyi"
#     b="qianer"
#     c="sunsan"
#     print("f3 has been executed!")
#     print(a)
#     print(b)
#     print(c)
#     def function4():
#         a="lisi"
#         print("The F4 in F3 has been executed!")
#         print(a)
#         print(b)
#         print(c)
#         def function5():
#             a="zhouwu"
#             b="wuliu"
#             print("The F5 in F4 has been executed!")
#             print(a)
#             print(b)
#             print(c)
#         function5()
#     function4()
# function3()
#
# #Anonymous function, used for simple calculation
# func=lambda a,b:a+b
# result=func(1,2)
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