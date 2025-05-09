# UPDATE `user` SET `name` = 'zoo', `email` = 'zoo@gmail.com', `password` = 'zoo@123' WHERE `user`.`id` = 4;

import mysql.connector


host="localhost"
user="root"
password=""
dbname="bank"
port=3307

conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
id=int(input("Enter update user id: "))
name=str(input("Enter username: "))
email=str(input("Enter Email: "))
passwd=str(input("Enter password: "))

cursor=conn.cursor()
query="UPDATE `user` SET `name` = %s, `email` = %s, `password` = %s WHERE `user`.`id` = %s;"
data=(name,email,passwd,id)
cursor.execute(query,data)
conn.commit()
print("update successfully")
conn.close()