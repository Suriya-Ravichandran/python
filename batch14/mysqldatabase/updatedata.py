import mysql.connector

hostname="localhost"
user="root"
password=""
dbname="batch14"
port=3307

try:
    conn=mysql.connector.connect(host=hostname,user=user,password=password,database=dbname,port=port)
    id=int(input("Enter your Id to update: "))
    name=str(input("Enter your Name: "))
    email=str(input("Enter your Email: "))
    passwd=str(input("Enter your password: "))

    cursor=conn.cursor()
    query="UPDATE `user` SET `name` = %s, `email` = %s, `password` = %s WHERE `user`.`id` = %s;"
    value=(name,email,passwd,id)
    cursor.execute(query,value)
    conn.commit()
    print("Data update successfully")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)


# DELETE FROM `user` WHERE `user`.`id` = 4