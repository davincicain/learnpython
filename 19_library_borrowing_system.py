import json
import datetime

#create user list
user_list='[{"user_account":"","user_password":"","user_name":"","user_type":""}]'
with open(r'.\reference1\user_list','w') as f:
    f.write(user_list)

#create book list
book_list='[{"book_code":0,"book_name":"","book_author":"","book_state":""}]'
with open(r'.\reference1\book_list','w') as f:
    f.write(book_list)

#borrowing information
borrowing_list='[{"book_name":"","book_borrower":"","lending_time":"","due_time":""}]'
with open(r'.\reference1\borrowing_list','w') as f:
    f.write(borrowing_list)

#user information
user_data={}

#read data
def read(file):
    with open(file,'r') as f:
        json_data = f.read()
    python_data = json.loads(json_data)
    return python_data

#write data
def write(python_data,file):
    json_data = json.dumps(python_data,ensure_ascii=False)
    with open(file,'w') as f:
        f.write(json_data)

#user login
def login():
    global user_data
    msg='fail'
    user_list=read(r'.\reference1\user_list')
    user_account=input('please input your account: ')
    user_password=input('please input your password: ')
    for user in user_list:
        if user["user_account"]==user_account and user["user_password"]==user_password:
            print('login success')
            msg='success'
            user_data=user
            break
    if msg=='fail':
        print('login fail')
    return msg

#show book list
def showBookList():
    book_list=read(r'.\reference1\book_list')
    print('--------------------------------------------------')
    for book in book_list:
        print(f"{book["book_code"]}     {book["book_name"]}     {book["book_author"]}     {book["book_state"]}")
    print('--------------------------------------------------')

#add book
def addBook():
    if user_data["user_type"]=='admin':
        print("you don't have permission")
        return
    book_list=read(r'.\reference1\book_list')
    book_code_list=[]
    for book in book_list:
        book_code_list.append(book["book_code"])
    book_code=max(book_code_list)+1
    book_name=input('please input your book name: ')
    book_author=input('please input your book author: ')
    book_state="available for borrowing"
    new_book={"book_code":book_code,"book_name":book_name,"book_author":book_author,"book_state":book_state}
    book_list.append(new_book)
    write(book_list,r'.\reference1\book_list')
    print('book add success')

#add book
def deleteBook():
    if user_data["user_type"]=='admin':
        print("you don't have permission")
        return
    book_list=read(r'.\reference1\book_list')
    book_code=int(input('please input your book code: '))
    exist=0
    for book in book_list:
        if book["book_code"]==book_code:
            exist = 1
            if book["book_state"]=="already borrowed":
                print("the book has already been borrowed")
                break
            book_list.remove(book)
            write(book_list, r'.\reference1\book_list')
            print('delete success')
            break
    if exist==0:
        print('book code not exist')

#lend book
def lend_book():
    current_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return_time=datetime.datetime.now()+datetime.timedelta(days=30)
    return_time=return_time.strftime('%Y-%m-%d %H:%M:%S')
    book_list=read(r'.\reference1\book_list')
    book_code=int(input('Please input the book code of the book you want to borrow: '))
    exist = 0
    for book in book_list:
        if book["book_code"]==book_code:
            exist = 1
            if book["book_state"]=="available for borrowing":
                print("The book borrowing is successful")
                #update book state
                book["book_state"]="already borrowed"
                write(book_list,r'.\reference1\book_list')
                #update borrowing data
                borrowing_list=read(r'.\reference1\borrowing_list')
                borrowing_data={"book_name":book["book_name"], "book_borrower":user_data["user_name"], "lending_time":current_time, "due_time":return_time}
                borrowing_list.append(borrowing_data)
                write(borrowing_list,r'.\reference1\borrowing_list')
                break
            else:
                print("the book has already been borrowed")
                break
    if exist==0:
        print('book code not exist')



def main():
    login()
    lend_book()

if __name__ == '__main__':
    main()