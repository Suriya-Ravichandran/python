# INSERT INTO `user` (`id`, `name`, `email`, `password`, `age`) VALUES ('2', 'boo', 'boo@gmail.com', 'boo@123', '21');
# SELECT * FROM `user`

import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch10"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    # print("Connection Sucessfully")
    name=str(input("Enter user name: "))
    email=str(input("Enter user name: "))
    passwd=str(input("Enter user password: "))
    age=int(input("Enter age: "))
    cursor=conn.cursor()


    query="INSERT INTO `user` (`name`, `email`, `password`, `age`) VALUES (%s, %s, %s, %s);"
    val=(name,email,passwd,age)
    cursor.execute(query,val)
    conn.commit()
    print("data insert successfully")
    conn.close()


except Exception as e:
    print(f"Error: {e}")