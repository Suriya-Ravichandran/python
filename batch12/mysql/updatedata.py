import mysql.connector

host="localhost"
user="root"
password=""
database="batch12"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)

    id=int(input("Enter user id to update: "))
    name=str(input("Enter user name: "))
    email=str(input("Enter user email: "))
    passwd=str(input("Enter passsword: "))
    cursor=conn.cursor()
    query="UPDATE `user` SET `name` = %s, `email` = %s, `password` = %s WHERE `user`.`id` = %s;"
    values=(name,email,passwd,id)
    cursor.execute(query,values)
    print("Data update succesfully")
    conn.commit()
    conn.close()
except Exception as e:
    print(e)