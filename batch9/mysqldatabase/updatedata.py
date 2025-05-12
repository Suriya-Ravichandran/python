# UPDATE `user` SET `name` = 'zoo', `email` = 'zoo@gmail.com', `password[` = 'zoo@123' WHERE `user`.`id` = 4;

import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch9"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    # print("Connection successfull")
    id=int(input("Enter update userid: "))
    name=str(input("Enter Username: "))
    email=str(input("Enter email: "))
    passwd=str(input("Enter passwd: "))
    cursor=conn.cursor()
    query="UPDATE `user` SET `name` = %s, `email` = %s, `password[` = %s WHERE `user`.`id` = %s;"
    value=(name,email,passwd,id)
    cursor.execute(query,value)
    print("update datasuccessfully")
    conn.commit()
    conn.close()

except Exception as e:
    print(f"Error: {e}")