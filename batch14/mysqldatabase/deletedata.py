import mysql.connector

hostname="localhost"
user="root"
password=""
dbname="batch14"
port=3307

try:
    conn=mysql.connector.connect(host=hostname,user=user,password=password,database=dbname,port=port)
    id=int(input("Enter your Id to Delete: "))
    cursor=conn.cursor()
    query="DELETE FROM `user` WHERE `user`.`id` = %s"
    value=(id,)
    cursor.execute(query,value)
    conn.commit()
    print("Data delete successfully")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)

