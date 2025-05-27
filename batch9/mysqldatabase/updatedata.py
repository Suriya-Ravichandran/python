import mysql.connector

host="localhost"
user="root"
password=""
port=3307
dbname="batch9"

try:
    id=int(input("Enter Userid to update: "))
    name=str(input("Enter Username: "))
    email=str(input("Enter Email: "))
    passwd=str(input("Enter password: "))

    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="UPDATE `user` SET `name` = %s, `email` = %s, `password[` = %s WHERE `user`.`id` = %s;"
    value=(name,email,passwd,id)
    cursor.execute(query,value)
    conn.commit()
    print("updated data successfull")
    conn.close()
except Exception as e:
    print(f"Error: {e}")