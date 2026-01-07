#if-else: Choosing between two conditions.
money=int(input("Your bonus is "))
if money>1000:
    print("Happy!")
    print("Go and have hot pot.")
else:
    print("Sorry!")
    print("You have not enough money.")

#elif: Choosing among multiple conditions.
money=int(input("Your bonus is "))
if money>1000:
    print("Happy!")
    print("Go and have hot pot.")
elif money>800:
    print("Go and have barbecue.")
elif money>500:
    print("Go and have noodles.")
elif money>300:
    print("Go and have bread.")
else:
    print("Sorry!")
    print("You have not enough money.")

#Nested selection statement.
money=int(input("Your bonus is "))
day=input("What day is it today (1-7) ")
if money>1000:
    print("Happy!")
    print("Go and have hot pot.")
elif money>800:
    print("Go and have barbecue.")
    if day=="6" or day=="7":
        print("Let's go today.")
    else:
        print("Let's go for this weekend.")
elif money>500:
    print("Go and have noodles.")
elif money>300:
    print("Go and have bread.")
else:
    print("Sorry!")
    print("you have not enough money.")

#in: Use list in the selection statements.
month=int(input("Please enter the month(1-12): "))
if month in [3,4,5]:
    print("Spring")
elif month in [6,7,8]:
    print("Summer")
elif month in [9,10,11]:
    print("Autumn")
elif month in [12,1,2]:
    print("Winter")
else:
    print("Please enter a valid month.")

listMenu=["rice","meet","vegetable","soup"]
print("Welcome! Todays's menu:\n",listMenu)
choise=int(input("Please enter the number(1.add 2.delete):"))
dishname = input("Please enter the name of the dish:")
if choise==1:
    listMenu.append(dishname)
elif choise==2:
    listMenu.remove(dishname)
else:
    print("This function is not available.")
print("New menu:\n",listMenu)

#for loop, It is often used in loops where traversing containers or number of literations are known.
for _ in range(10):#"_"indicates a loop variable that is not used.
    print("hello, world!")

for i in range(1,11,2):#rang(initial value(include),end value(exclude),step size)
    print(f"第{i}次打印：hello, world!")
print("print end")#outside the loop

#summation
num=0
for i in range(1,101):
    num=num+i
print(num)

#loop throngh the container using a for loop
#direct traversal
listNames=["yi","er","san","si","wu","liu","qi","ba"]
for i in listNames:
    print(i)
for i in listNames:
    print(listNames)
for _ in listNames:
    print(_)
for _ in listNames:
    print(listNames)

#constract an index:
listNames=["yi","er","san","si","wu","liu","qi","ba"]
for idx in range(0,len(listNames)):
    print(listNames[idx])

#tuple traversal
listNames=("yi","er","san","si","wu","liu","qi","ba")
for idx in range(0,len(listNames)):
    print(listNames[idx])

#dictionary traversal: The dictionary has no index, so it can only be traversed directly.
userInfo={"name":"yi","age":1,"hobby":"basketball"}
for x in userInfo:
    print(x) #It will get only the keys when the direct traversal method is used for the dictionary.
for x in userInfo:
    print(userInfo[x])
for x in userInfo:
    print(x,userInfo[x])

#set traversal
seta={1,23,456,789}
for x in seta:
    print(x)#The set is disordered, so it will print a variable result.

#The combined application of selection structures and loop structures
names=["yi","er","san","si","wu","liu"]
key=input("Please input the name you want to search: ")
result="Not exist!"
for name in names:
    if name==key:
        result="Exist!"
print(result)

#while loop, It is often used in loops where the chonditions are konwn but the number of literations is unknown.
i=1
while i<=10:
    print(f"{i} Hello world!")
    i+=1

#nested loop
day=1
while day<=7:
    print(f"{day} day")
    i=1
    while i <= 10:
        print(f"{day} day {i} ")
        i+=1
    day+=1

lista=[0,1,2,3]
listb=[4,5,6]
listc=[7,8,9]
listd=[lista,listb,listc]
for i in listd:
    for j in i:
        print(j)
    print("----------")

#continue and break
for i in range(1,11):
    print(f"{i} year, I have repaid the loan.")
    if i==5:
        print(f"{i} year, I need not repay the loan.")
        continue #End this loop and continue the next loop.
    if i==10:
        print("I have already repaid the whole loan.")
        break #End the whole loop.

#infinite loop
i=1
while True:
    print(i)
    i+=1

#pass: Use it to reserve a position when you have no idea, and the program does not report an error.