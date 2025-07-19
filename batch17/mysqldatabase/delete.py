import mysql.connector
host="localhost"
user="root"
password=""
dbname="demo"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    id=int(input("Enter id to delete: "))
    cursor=conn.cursor()
    value=(id,)
    query="DELETE FROM `user` WHERE `user`.`id` = %s"
    cursor.execute(query,value)
    conn.commit()
    print("delete data sucessfully")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)