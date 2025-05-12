# DELETE FROM `user` WHERE `user`.`id` = 4

import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch9"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    # print("Connection successfull")
    id=int(input("Enter delete userid: "))
    
    cursor=conn.cursor()
    query="DELETE FROM `user` WHERE `user`.`id` = %s;"
    value=(id,)
    cursor.execute(query,value)
    print("delete datasuccessfully")
    conn.commit()
    conn.close()

except Exception as e:
    print(f"Error: {e}")