# DELETE FROM `user` WHERE `user`.`id` = 3

import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch10"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    # print("Connection Sucessfully")
    id=int(input("Enter user id to delete: "))
    cursor=conn.cursor()


    query="DELETE FROM `user` WHERE `user`.`id` = %s"
    val=(id,)
    cursor.execute(query,val)
    conn.commit()
    print("data delete successfully")
    conn.close()


except Exception as e:
    print(f"Error: {e}")