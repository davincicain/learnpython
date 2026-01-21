"""
NameError: the variable is not defined
SyntaxError: Invalid syntax, for example, there is a lack of a comma
IO Error: file operation error
ZeroDivisionError: division by zero
IndentationError: indentation problem
ModuleNotFoundError: the third party package is not installed
FileNotFoundError: file doesn't exist
AttributeError: the object doesn't have corresponding attributes and methods
IndexError: list index out of range
TypeError: invalid type for arguments
KeyError: invalid key of dictionary
"""

"""
#capture exception: when encountering an error, display the error message and continue executing the subsequent content
try:
    #code that may raise exceptions

except Exception as e:
    #code executed when an exception occurs

except TypeError as e: #exception can also be replaced by a direct error, for example, ZeroDivisionError, TypeError or others
    #code executed when an typeerror occurs

else:
    #code executed when there are no exceptions

finally:
    #code that will be executed whether there are exceptions or not
"""

def func(lista):
    for i in lista:
        try:
            result = 10 / i
            print(result)
        except Exception as e:
            print(e)
        else:
            print("this loop is executed normally")
        finally:
            print(f"the divisor in this case is {i}")

def mian():
    lista = [1, 2, 3, 0, 4, 5, 6, "a", 7, 8, 9, 10]
    func(lista)

if __name__ == '__main__':
    mian()

# custom exception: there are no exceptions in the program, but we want to throw an exception manually

class MyException(Exception):
    pass

def func():
    sex = input("please input your sex: ")
    if sex == "male" or sex == "female":
        print(f"your sex is {sex}")
    else:
        print("your input is wrong")
        ex = MyException("sex must be male or female") #create an exception object
        raise ex #throw exceptions

def main():
    try:
        func()
    except MyException as e:
        print("the argument is wrong")

if __name__ == "__main__":
    main()