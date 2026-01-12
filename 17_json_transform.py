import json

def main():

    #transform json to python
    json_student_1='{"name":"zhao","age":"1","hobby":"dance"}'

    json_student_list='[{"name":"zhao","age":"1","hobby":"piano"},\
                   {"name":"qian","age":"2","hobby":"chess"},\
                   {"name":"sun","age":"3","hobby":"write"},\
                   {"name":"li","age":"4","hobby":"draw"}]'

    python_data_1=json.loads(json_student_1)
    print(python_data_1)
    print(type(python_data_1))
    print(python_data_1["hobby"])

    python_data_2=json.loads(json_student_list)
    for student_name in python_data_2:
        print(student_name["name"])

    #transform python to json: dictionary, lists nested within dictionaries
    python_student_1={"name":"赵","age":"1","hobby":"dance"}

    json_data_1=json.dumps(python_student_1, ensure_ascii=False) #forbid ascii conversion
    print(json_data_1,type(json_data_1))

if __name__ == '__main__':
    main()