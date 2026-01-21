"""
account: root
password: 123456
port: 3306
"""

import pymysql
import random

#the shared method for obtaining a database connection
def getConnection():
    host = "localhost"
    port = 3306
    username = "root"
    password = "123456"
    db = "20260120"
    charset = "utf8mb4"

    #create a database connect object and establish a connection
    conn = pymysql.Connect(host=host, port=port, user=username, password=password, db=db, charset=charset)
    print("connect successfully")

    return conn


def main():
    #create a connection object
    conn=getConnection()
    #create a cursor object to execute sql statements and query the database
    cursor = conn.cursor()

    try: #the code of database operation
        #write sql statements, sql statements are strings
        #create table
        sql1='''
        CREATE TABLE stu (
            id int(11) NOT NULL AUTO_INCREMENT,
            name varchar(255) DEFAULT NULL,
            age int(11) DEFAULT NULL,
            hobby varchar(255) DEFAULT NULL,
            PRIMARY KEY (id)
            )
        '''

        #delete table
        sql2='drop table stu'

        #create data for a table
        sql3='INSERT INTO stu(name, age, hobby) VALUES("zhao", 1, "read")'

        name="qian"
        age=2
        hobby="write"

        sql4 =  f'''
        INSERT INTO stu(name, age, hobby) VALUES("{name}", {age}, "{hobby}")
        '''
        print(sql4)

        #execute sql statements
        cursor.execute(sql4)

        #submit data
        conn.commit()

        for i in range(100):
            name=random.choice(["zhao","qian","sun","li","zhou","wu","zheng","wang"])
            age=random.randint(1,8)
            hobby=random.choice(["music","speech","read","write","piano","poetry","","draw"])

            sql5 =  f'''
            INSERT INTO stu(name, age, hobby) VALUES("{name}", {age}, "{hobby}")
            '''

            cursor.execute(sql5)

            sql6 =  '''
            INSERT INTO stu(name, age, hobby) VALUES(%s, %s, %s)
            '''

            cursor.execute(sql6, (name, age, hobby))

            conn.commit()

        #update data
        sql7='UPDATE stu set hobby="poetry" WHERE hobby=""'
        cursor.execute(sql7)
        conn.commit()

        # delete data
        sql8 = 'DELETE FROM stu WHERE age=8'
        cursor.execute(sql8)
        conn.commit()

        #query data, needn't commit
        # get one line of data
        sql9='SELECT * FROM stu WHERE id=1'
        cursor.execute(sql9)
        data1=cursor.fetchone()
        print(data1)

        # get multiple lines of data
        sql10 = 'SELECT * FROM stu WHERE id>=5'
        cursor.execute(sql10)
        data2 = cursor.fetchall()
        print(data2)

        for stu in data2:
            print(stu[1])

    except Exception as e:
        print(e)
    finally: #it will close the connection whatever exceptions occur
        cursor.close() #close cursor
        conn.close() #close connection

if __name__ == '__main__':
    main()