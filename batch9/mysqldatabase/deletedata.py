# DELETE FROM `user` WHERE `user`.`id` = 6

import mysql.connector

host="localhost"
user="root"
password=""
port=3307
dbname="batch9"

try:
    email=str(input("Enter Email: "))

    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="DELETE FROM `user` WHERE `user`.`email` = %s"
    value=(email,)
    cursor.execute(query,value)
    conn.commit()
    print("delete data successfull")
    conn.close()
except Exception as e:
    print(f"Error: {e}")