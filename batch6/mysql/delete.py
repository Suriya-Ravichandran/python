# DELETE FROM `user` WHERE `user`.`id` = 3


import mysql.connector

host="localhost"
user="root"
password=""
dbname="umarani"

conn = mysql.connector.connect(host=host,user=user,password=password,database=dbname)

id=int(input("Enter delete userid: "))

cursor=conn.cursor()
query="DELETE FROM `user` WHERE `user`.`id` = %s"
val=(id,)
cursor.execute(query,val)
conn.commit()
print("delete data successfully")