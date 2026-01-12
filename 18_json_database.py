import json
from ctypes import pythonapi

# create a database file
json_user_list_1 = '[{"user_name":"zhao","user_password":"1"},{"user_name":"qian","user_password":"2"}]'
with open(r'.\reference1\users.txt', 'w', encoding='utf-8') as f1:
    f1.write(json_user_list_1)

#query operation: write a code for reading data
def read1():
    with open(r'.\reference1\users.txt','r',encoding='utf-8') as f2:
        json_user_list_2 = f2.read()
        python_user_list_1=json.loads(json_user_list_2)
    return python_user_list_1

#write operation: write a code for writing data
def write1(python_user_list_3):
    json_user_list_3=json.dumps(python_user_list_3,ensure_ascii=False)
    with open(r'.\reference1\users.txt','w',encoding='utf-8') as f3:
        f3.write(json_user_list_3)

def register1():
    user_name_1=input('please input a new user name: ')
    user_password_1=input('please input a new user password: ')
    new_user_1={"user_name":user_name_1, "user_password": user_password_1}
    python_user_list_4=read1()

    for user_1 in python_user_list_4:
        if user_1['user_name']==user_name_1:
            print('user_name already exists')
            return
    python_user_list_4.append(new_user_1)
    write1(python_user_list_4)

def main():
    register1()

if __name__ == '__main__':
    main()