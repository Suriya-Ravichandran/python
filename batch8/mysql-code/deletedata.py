# DELETE FROM `user` WHERE `user`.`id` = 4

import mysql.connector


host="localhost"
user="root"
password=""
dbname="bank"
port=3307

conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
id=int(input("Enter Delete user id: "))
cursor=conn.cursor()
query="DELETE FROM `user` WHERE `user`.`id` = %s;"
data=(id,)
cursor.execute(query,data)
conn.commit()
print("Delete successfully")
conn.close()