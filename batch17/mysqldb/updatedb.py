

import mysql.connector

host=""
user=""
password=""
dbname=""
port=3306

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()

    userid=int(input("Enter update user id: "))
    name=str(input("Enter your name: "))
    email=str(input("Enter your email: "))
    passwd=str(input("Enter your password: "))

    value=(name,email,passwd,userid)
    query="UPDATE `user` SET `name` = %s, `email` = %s, `password` = %s WHERE `id` = %s;"
    cursor.execute(query,value)
    conn.commit()
    print("update successfully")
    conn.close()
except Exception as e:
    print(f"Error: {e}")