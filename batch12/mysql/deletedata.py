import mysql.connector

host="localhost"
user="root"
password=""
database="batch12"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)

    id=int(input("Enter user id to Delete: "))
    cursor=conn.cursor()
    query="DELETE FROM `user` WHERE `user`.`id` = %s"
    values=(id,)
    cursor.execute(query,values)
    print("Data delete succesfully")
    conn.commit()
    conn.close()
except Exception as e:
    print(e)