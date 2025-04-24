# UPDATE `user` SET `name` = 'fooboo' WHERE `user`.`id` = 2;

import mysql.connector

host="localhost"
user="root"
password=""
dbname="umarani"

conn = mysql.connector.connect(host=host,user=user,password=password,database=dbname)

id=int(input("Enter id: "))
name=str(input("Enter Name: "))

cursor=conn.cursor()
query="UPDATE `user` SET `name` = %s WHERE `user`.`id` = %s;"
val=(name,id)
cursor.execute(query,val)
conn.commit()
print("update data successfully")
