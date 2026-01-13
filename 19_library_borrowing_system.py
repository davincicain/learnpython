import json

#create user list
user_list='[{"user_account":"","user_password":"","user_name":"","user_type":"",}]'
with open(r'.\reference1\user_list','w') as f:
    f.write(user_list)

#create book list
book_list='[{"book_code":"","book_name":"","book_author":"","book_state":"",}]'
with open(r'.\reference1\book_list','w') as f:
    f.write(book_list)

#borrowing information
borrowing_data='[{"book_name":"","book_borrower":"","lending_time":"","due_time":""}]'
with open(r'.\reference1\borrowing_data','w') as f:
    f.write(borrowing_data)

#user information
user_data={}

#read data
def read(file):
    with open(file,'r') as f:
        json_data = f.read()
    python_data = json.loads(json_data)
    return python_data

#write data
def write1(python_data,file):
    json_data = json.dumps(python_data,ensure_ascii=False)
    with open(file,'w') as f:
        f.write(json_data)

#user login
def login():
    global user_data
    msg='fail'
    user_list=read(r'.\reference1\user_list')
    user_account=print('please input your account: ')
    user_password=input('please input your password: ')
    for user in user_list:
        if user["user_account"]==user_account and user["user_password"]==user_password:
            print('login success')
            msg='success'
            break
    if msg=='fail':
        print('login fail')
    return msg

#show book list
def showBookList():
    book_list=read(r'.\reference1\book_list')
    print('--------------------------------------------------')
    for book in book_list:
        print(f"{book["book_code"]}     {book["book_name"]}     {book["book_borrower"]}     {book["book_state"]}")
    print('--------------------------------------------------')

#add book
def addBook():
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
    write1(book_list,r'.\reference1\book_list')
    print('book add success')

#add book
def deleteBook():
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
            write1(book_list, r'.\reference1\book_list')
            print('delete success')
            break

    if exist==0:
        print('book code not exist')


def main():
    showBookList()
    addBook()
    showBookList()
    deleteBook()
    showBookList()

if __name__ == '__main__':
    main()