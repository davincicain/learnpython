#define a class
class Cat: #the first letter of the class name should be capitalized
    #initialize method
    def __init__(self): #self: attribute name,define attribute
        #attribute: nick,color,age
        self.nick="kitte"
        self.color="white"
        self.age=1
    def eat(self):
        print(f"eat fishes ")
    def sleep(self):
        print("sleeping")

class Book:
    def __init__(self,id,name,author):
        self.id=id
        self.name=name
        self.author=author
    def show(self,page_number):
        print(f"show {page_number} of book information")
        return "have finished showing"
    def update(self):
        print(self.name,"update book information") #self: implicitly pass the current object

def main():
    #create an object
    cat1 = Cat()
    book1=Book(1,"chinese","zhao")
    book2=Book(2,"mathematics","qian")

    #obtain an attribute value
    print(cat1.nick)
    print(book1.id)
    print(book2.name)

    #modify an attribute value
    cat1.nick="miaomiao"
    print(cat1.nick)

    #call the method of an object
    cat1.eat()
    book1.show(3)

    result = book1.show(5)
    print(result)

    book1.update()
    book2.update()

if __name__ == '__main__':
    main()