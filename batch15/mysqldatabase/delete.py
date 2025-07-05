

import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch15"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    id=int(input("Enter your id to update: "))
    cursor=conn.cursor()
    values=(id,)
    query="DELETE FROM `user` WHERE `user`.`id` = %s"
    cursor.execute(query,values)
    cursor.close()
    conn.commit()
    conn.close()
    print("Data delete successfully")
except Exception as e:
    print(e)