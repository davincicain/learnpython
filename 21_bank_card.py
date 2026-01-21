class Card:
    def __init__(self,account,password,name,balance):
        self.account = account
        self.password = password
        self.name = name
        self.__balance = balance #__: private attributes can not be accessed directly
        self.bank="Construction Bank" #default values can be entered directly

    def login(self):
        account=input("please input your account: ")
        password=input("please input your password: ")
        if account==self.account and password==self.password:
            print("login success")
            return "ok"
        else:
            print("login fail")
            return "no"

    def show(self):
        result=self.login() #use other methods in the class
        if result=="ok":
            print(f"your balance is: {self.__balance}")

    def deposit(self):
        result=self.login()
        if result=="ok":
            money=float(input("please input your deposit money: "))
            if money>=10000:
                self.__reword()
            self.__balance+=money
            print(f"deposit {money} success, your balance is: {self.__balance}")

    def __reword(self): #__: private methods can not be accessed directly
        print("reword a phone")

def main():
    card1 = Card("001","aaa","zhao",100)
    card2 = Card("002","bbb","qian",200)

    card1.deposit()
    card2.show()

    # print(card1.__balance) #private attributes can only be called through methods.
    card1.show()

    # card1.__reword() #private methods can only be called through other methods.
    card1.deposit()

    print(card1._Card__balance) #private attributes in python can also be used directly, but they are not commonly used.

if __name__ == "__main__":
    main()