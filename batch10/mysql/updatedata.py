# UPDATE `user` SET `name` = 'zoo', `email` = 'zoo@gmail.com', `password` = 'zoo@123' WHERE `user`.`id` = 3;

import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch10"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    # print("Connection Sucessfully")
    id=int(input("Enter user id to update: "))
    name=str(input("Enter user name: "))
    email=str(input("Enter user name: "))
    passwd=str(input("Enter user password: "))
    age=int(input("Enter age: "))
    cursor=conn.cursor()


    query="UPDATE `user` SET `name` = %s, `email` = %s, `password` = %s,`age`= %s WHERE `user`.`id` = %s;"
    val=(name,email,passwd,age,id)
    cursor.execute(query,val)
    conn.commit()
    print("data update successfully")
    conn.close()


except Exception as e:
    print(f"Error: {e}")