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