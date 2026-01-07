"""
random: getting random numbers
time: time management
os: operating system
sys: python system module
json: processing json data
datetime: processing date and time
math: provide mathematical functions and constants
urllib: construct a request and obtain response information
"""

import sys #methods of interacting with the python interpreter

for i in range(1,1000):
    print(i)
    if i==500:
        sys.exit() #end all programs
print("program end") #this command will not be executed

import sys as aaa

for i in range(1,1000):
    print(i)
    if i==500:
        aaa.exit() #end all programs
print("program end") #this command will not be executed

import os
print(os.path.exists(r"D:\shaojun3\Desktop\py\reference1")) #path module is a sub-module under the os module

from os import path #directly importing the path module can save memory
print(path.exists(r"D:\shaojun3\Desktop\py\reference1"))

import random
def main():
    a = random.randint(1, 6) #generate a random integer
    print(a)

    b = random.uniform(1, 3) #generate a random float
    print(b)

    lista = ["zhao","qian","sun","li","zhou","wu","zheng","wang"]
    name = random.choice(lista)
    print(name)

if __name__ == '__main__':
    main()

import time
def main():
    a = time.time() #record timestamp: the number of seconds from the current execution time minus the time at 0:00 on january 1, 1930
    print(a)
    for i in range(1,10000):
        print(i)
    b = time.time()
    print(b)
    print(b-a)#used to obtain program running time

    c = time.localtime() #obtain local system time
    print(c)

    d = time.asctime(c) #format
    print(d)

    e = time.strftime("%Y年%m月%d日 %H:%M:%S",c) #customize the conversion format
    print(e)

    print("program is running")
    time.sleep(5) #the program goes to sleep
    print("program completed")

if __name__ == '__main__':
    main()

import datetime
def main():
    a = datetime.datetime.now() #obtain current date and time
    print(a)

    b = a.strftime("%Y年%m月%d日 %H:%M:%S") #translate data to string
    print(b)

    c = "2012/12/12 12:12:12"
    d = datetime.datetime.strptime(c, "%Y/%m/%d %H:%M:%S") #translate string to date
    print(d)

    e = datetime.datetime(2001,1,1,1,1,1,1) #obtain the specified time
    print(e)

    f = e+datetime.timedelta(days=1)
    print(f)
    g = f+datetime.timedelta(hours=-1)
    print(g)

if __name__ == '__main__':
    main()

import math
def main():
    a = 25
    b = math.sqrt(a) #square root
    print(b)

    c = 5
    print(math.factorial(c)) #factorial

    d = math.pi #obtain pi
    print(d)

if __name__ == '__main__':
    main()

from urllib import request
def main():
    url = "http://www.baidu.com"
    a = request.urlopen(url).read() #send a request and get a response information
    print(a.decode('utf-8'))

if __name__ == '__main__':
    main()