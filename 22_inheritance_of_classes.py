class Animal:
    def __init__(self, nick, color, age):
        self.nick = nick
        self.color = color
        self.age = age
    def run(self):
        print("Animal is running...")
    def eat(self):
        print("Animal is eating...")

class Dog(Animal): #inherit from the parent class
    def run(self): # method overriding
        print("Dog is running...")
    def sleep(self):
        print("Dog is sleeping...")

class Husky(Dog):pass

class   Pet:
    def __init__(self, strain):
        self.strain = strain
    def play(self):
        print("Pet is playing...")

class Cat(Animal,Pet): #multiple inheritance, call attributes and methods in Breadth-first sequence
    pass

def main():
    dog=Dog("wangwang","black","2")
    dog.eat()
    dog.run()
    dog.sleep()

    husky=Husky("haha","grey","3") #inheritance can be passed on
    husky.run()

    cat=Cat("kitty","white",1)
    cat.eat()

if __name__ == "__main__":
    main()