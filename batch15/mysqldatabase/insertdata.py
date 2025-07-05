import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch15"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    name=str(input("Enter username: "))
    email=str(input("Enter Email: "))
    passwd=str(input("Password: "))
    cursor=conn.cursor()
    values=(name,email,passwd)
    query="INSERT INTO `user` (`name`, `email`, `password`) VALUES (%s, %s, %s);"
    cursor.execute(query,values)
    cursor.close()
    conn.commit()
    conn.close()
    print("Data insert successfully")
except Exception as e:
    print(e)