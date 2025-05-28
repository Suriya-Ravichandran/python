import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch11"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    id=int(input("Enter user id to Delete: "))
    cursor=conn.cursor()
    query="DELETE FROM `user` WHERE `user`.`id` = %s"
    value=(id,)
    cursor.execute(query,value)
    conn.commit()
    conn.close()
    print("Data delete sucessfully")

except Exception as e:
    print(f"Error: {e}")