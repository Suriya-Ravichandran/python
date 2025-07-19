# UPDATE `user` SET `name` = 'foo', `email` = 'boo@gmail.com', `password` = 'boo@123' WHERE `user`.`id` = 1;

import mysql.connector

host="localhost"
user="root"
password=""
dbname="demo"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    id=int(input("Enter id to update: "))
    name=str(input("Enter name: "))
    email=str(input("Enter email: "))
    passwd=str(input("Enter password: "))
    cursor=conn.cursor()
    value=(name,email,passwd,id)
    query="UPDATE `user` SET `name` = %s, `email` = %s, `password` = %s WHERE `user`.`id` = %s;"
    cursor.execute(query,value)
    conn.commit()
    print("update data sucessfully")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)