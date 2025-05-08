# DELETE FROM `user` WHERE `user`.`id` = 5

import mysql.connector


host="localhost"
user="root"
password=""
dbname="batch7"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    print("Connection successfully")
    refers=conn.cursor()
    query="DELETE FROM `user` WHERE `user`.`id` = %s"
    values=(4,)
    refers.execute(query,values)
    print("delete Data success")
    conn.commit()
    conn.close()
except mysql.connector.errors.DatabaseError:
    print("Connection failed")