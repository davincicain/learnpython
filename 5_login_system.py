# account1={"name":"yi","accountName":"aaa","password":"111","balance":10000}
# account2={"name":"er","accountName":"bbb","password":"222","balance":20000}
# account3={"name":"san","accountName":"ccc","password":"333","balance":30000}
# account4={"name":"si","accountName":"ddd","password":"444","balance":40000}
# account5={"name":"wu","accountName":"eee","password":"555","balance":50000}
# account6={"name":"liu","accountName":"fff","password":"666","balance":60000}
# account7={"name":"qi","accountName":"ggg","password":"777","balance":70000}
# account8={"name":"ba","accountName":"hhh","password":"888","balance":80000}
# accountList=[account1,account2,account3,account4,account5,account6,account7,account8]
#
# for login_count in range(len(accountList)):
#     userAccount = str(input("Please enter your account number: "))
#     userPassword = str(input("Please enter your password: "))
#     for loginAccount in accountList:
#         if userAccount == loginAccount["accountName"] and userPassword == loginAccount["password"]:
#             break
#     if userAccount == loginAccount["accountName"] and userPassword == loginAccount["password"]:
#         print("Login successful!")
#         # break
#     elif login_count < 2:
#         print(f"You have made {login_count + 1} mistakes, please enter again!")
#         continue
#     else:
#         print(f"You have made {login_count + 1} mistakes, your account has been locked!")
#         break
#
#     while True:
#         functionNumber = int(input("Please enter the function number( 1.query 2.transfer money 3.recharge 4.exist): "))
#         if functionNumber == 1:
#             print(loginAccount)
#         elif functionNumber == 2:
#             while True:
#                 partyAccount = input("Please enter the other party's account name: ")
#                 transferAmount = float(input("Please enter transfer amount: "))
#                 msg1 = 0 # It is used to record whether the entered party's account is correct.
#                 msg2 = 0 # It is used to record whether the entered transfer amount is correct.
#                 for objectAccount in accountList:
#                     if partyAccount == objectAccount["accountName"]:
#                         msg1 = 1
#                         break
#                 if msg1 == 1:
#                     if transferAmount <= loginAccount["balance"]:
#                         loginAccount["balance"] -= transferAmount
#                         objectAccount["balance"] += transferAmount
#                         print(f"The transfer was successful! Balance is {loginAccount["balance"]} now!")
#                         msg2 = 1
#                         break
#                 if msg2 == 1:
#                     break
#                 if msg1 == 0:
#                     print("The party's account name is not correct! Please enter again!")
#                     break
#                 if msg2 == 0:
#                     print("balance is lacking! Please enter again!")
#                     break
#         elif functionNumber == 3:
#             while True:
#                 rechargeAmount = float(input("Please enter the recharge amount: "))
#                 if rechargeAmount <= 0:
#                     print("The recharge amount must be greater than zero! Please enter again!")
#                 else:
#                     loginAccount["balance"] += rechargeAmount
#                     print(f"Recharge was successful! Balance is {loginAccount["balance"]} now!")
#                     break
#         elif functionNumber == 4:
#             break
#         else:
#             print("There is no such function, please enter again!")