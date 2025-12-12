# #user information
# user1 = {"account":"aaa","password":"111","name":"yi","role":"clerk"}
# user2 = {"account":"bbb","password":"222","name":"er","role":"clerk"}
# user3 = {"account":"ccc","password":"333","name":"san","role":"manager"}
# users_list = [user1,user2,user3]
#
# #menu
# food1 = {"number":1,"name":"chicken","price":100,"stock":1,"updater":"yi"}
# food2 = {"number":2,"name":"duck","price":200,"stock":2,"updater":"er"}
# food3 = {"number":3,"name":"fish","price":300,"stock":3,"updater":"san"}
# food4 = {"number":4,"name":"meet","price":400,"stock":4,"updater":"si"}
# food5 = {"number":5,"name":"alcohol","price":500,"stock":5,"updater":"wu"}
# food_list = [food1,food2,food3,food4,food5]
#
# #global variable
# current_user = {}
#
# #only manager can use it
# def check_manager(fun):
#     def wrapper():
#         if current_user["role"] == "manager":
#             fun()
#         else:
#             print("You don't have the permission to modify!")
#     return wrapper
#
# #login
# def login():
#     global current_user
#     login_status = "failure"
#     user_account = input("Please input your account: ")
#     user_password = input("Please input your password: ")
#     for user in users_list:
#         if user["account"] == user_account and user["password"] == user_password:
#             login_status = "success"
#             current_user = user
#     return login_status
#
# #display menu
# def menu():
#     for food in food_list:
#         print(f"number: {food["number"]}     name: {food["name"]}     price: {food["price"]}     stock: {food["stock"]}     updater: {food["updater"]}")
#
# #query food information
# def query_food_by_name():
#     food_name = input("Please input your food name: ")
#     food_exist = False
#     for food in food_list:
#         if food_name == food["name"]:
#             print(f"number: {food["number"]}     name: {food["name"]}     price: {food["price"]}     stock: {food["stock"]}")
#             food_exist = True
#     if food_exist == False:
#         print("Food doesn't exist!")
#
# #add food
# @check_manager
# def add_food():
#     food_number_list = []#generate a new number
#     for food in food_list:
#         food_number_list.append(food["number"])
#     new_food_number = max(food_number_list)+1
#     new_food_name = input("Please input your new food name: ")
#     new_food_price = float(input("Please input your new food price: "))
#     new_food_stock = int(input("Please input your new food stock: "))
#     new_food = {"number":new_food_number,"name":new_food_name,"price":new_food_price,"stock":new_food_stock,"updater":current_user["name"]}
#     food_list.append(new_food)
#     menu()
#
# #delete food
# @check_manager
# def delete_food():
#     food_number = int(input("Please input your food number: "))
#     food_exist = False
#     for food in food_list:
#         if food["number"] == food_number:
#             food_exist = True
#             food_list.remove(food)
#     if food_exist == False:
#         print("Food doesn't exist!")
#     menu()
#
# #set food information
# # noinspection PyTypeChecker
# @check_manager
# def update_food():
#     food_exist = False
#     food_number = int(input("Please input your food number: "))
#     for food in food_list:
#         if food["number"] == food_number:
#             food_exist = True
#             update_content = int(input("Please input the content you want to update(1.price 2.stock): "))
#             if update_content == 1:
#                 update_price = float(input("Please input your new price: "))
#                 food["price"] = update_price
#             elif update_content == 2:
#                 update_stock = int(input("Please input your new stock: "))
#                 food["stock"] = update_stock
#             else:
#                 print("Invalid input!")
#     if food_exist == False:
#         print("Food doesn't exist!")
#     menu()
#
# #inventory warning
# def inventory_warning():
#     food_stock_status = False
#     for food in food_list:
#         if food["stock"]<3:
#             food_stock_status = True
#             print(f"{food}")
#     if food_stock_status == False:
#         print("Food doesn't need to replenish the stock!")
#
# #sort by price
# def sort_by_price():
#     sort_choice = int(input("Please input your choice(1.ascend 2.desceng): "))
#     price_list = []
#     for food in food_list:
#         price_list.append(food["price"])
#     price_list = list(set(price_list))
#     if sort_choice == 1:
#         price_list.sort()
#     elif sort_choice == 2:
#         price_list.sort(reverse=True)
#     for price in price_list:
#         for food in food_list:
#             if food["price"] == price:
#                 print(f"{food}")
#
# #business logic
# print("--------------------ordering system--------------------")
# while True:
#     login_status = login()
#     if login_status == "failure":
#         print("Login failed! please try again!")
#         continue
#     while True:
#         print("--------------------function list--------------------")
#         print("1.menu")
#         print("2.query food by name")
#         print("3.add food")
#         print("4.delete food")
#         print("5.update food")
#         print("6.inventory warning")
#         print("7.sort by price")
#         print("8.exit")
#         choice=int(input("Please enter your choice: "))
#         if choice == 1:
#             menu()
#         elif choice == 2:
#             query_food_by_name()
#         elif choice == 3:
#             add_food()
#         elif choice == 4:
#             delete_food()
#         elif choice == 5:
#             update_food()
#         elif choice == 6:
#             inventory_warning()
#         elif choice == 7:
#             sort_by_price()
#         elif choice == 8:
#             break
#         else:
#             print("Invalid choice, please try again!")
#             continue

# def add(a, b):
#     return a + b
#
# # 定义一个"包装函数"，接收函数作为参数
# def wrapper(func, x, y):
#     print(f"即将执行函数：{func.__name__}")
#     result = func(x, y)  # 执行传入的函数
#     print(f"函数执行结果：{result}")
#     return result
#
# wrapper(add, 2, 3)

def outer(msg):
    # 内部函数
    def inner():
        print(f"内部函数执行：{msg}")
    return inner  # 返回内部函数（不执行）

# 调用outer，得到inner函数
f = outer("hello 装饰器")
f()  # 执行inner函数