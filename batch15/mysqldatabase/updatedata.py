


import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch15"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    id=int(input("Enter your id to update: "))
    name=str(input("Enter username: "))
    email=str(input("Enter Email: "))
    passwd=str(input("Password: "))
    cursor=conn.cursor()
    values=(name,email,passwd,id)
    query="UPDATE `user` SET `name` = %s, `email` = %s, `password` = %s WHERE `user`.`id` = %s;"
    cursor.execute(query,values)
    cursor.close()
    conn.commit()
    conn.close()
    print("Data update successfully")
except Exception as e:
    print(e)