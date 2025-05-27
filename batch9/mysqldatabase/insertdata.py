import mysql.connector

host="localhost"
user="root"
password=""
port=3307
dbname="batch9"

try:
    name=str(input("Enter Username: "))
    email=str(input("Enter Email: "))
    passwd=str(input("Enter password: "))

    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="INSERT INTO `user` (`name`, `email`, `password[`) VALUES (%s, %s, %s);"
    value=(name,email,passwd)
    cursor.execute(query,value)
    conn.commit()
    print("Insert data successfull")
    conn.close()
except Exception as e:
    print(f"Error: {e}")