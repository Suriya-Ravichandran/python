import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch11"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    id=int(input("Enter user id to modify: "))
    name=str(input("Enter username: "))
    email=str(input("Enter user email: "))
    password=str(input("Enter password: "))
    cursor=conn.cursor()
    query="UPDATE `user` SET `name` = %s, `email` = %s, `password` = %s WHERE `user`.`id` = %s;"
    value=(name,email,password,id)
    cursor.execute(query,value)
    conn.commit()
    conn.close()
    print("Data update sucessfully")

except Exception as e:
    print(f"Error: {e}")