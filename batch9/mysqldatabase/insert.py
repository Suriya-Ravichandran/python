#INSERT INTO `user` (`id`, `name`, `email`, `password[`) VALUES ('1', 'foo', 'foo@gmail.com', 'foo@123');

import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch9"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    # print("Connection successfull")
    name=str(input("Enter Username: "))
    email=str(input("Enter email: "))
    passwd=str(input("Enter passwd: "))
    cursor=conn.cursor()
    query="INSERT INTO `user` (`name`, `email`, `password[`) VALUES (%s, %s, %s);"
    value=(name,email,passwd)
    cursor.execute(query,value)
    print("Insert datasuccessfully")
    conn.commit()
    conn.close()

except Exception as e:
    print(f"Error: {e}")