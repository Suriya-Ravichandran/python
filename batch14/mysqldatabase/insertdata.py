import mysql.connector

hostname="localhost"
user="root"
password=""
dbname="batch14"
port=3307

try:
    conn=mysql.connector.connect(host=hostname,user=user,password=password,database=dbname,port=port)

    name=str(input("Enter your Name: "))
    email=str(input("Enter your Email: "))
    passwd=str(input("Enter your password: "))

    cursor=conn.cursor()
    query="INSERT INTO `user` (`name`, `email`, `password`) VALUES (%s, %s, %s);"
    value=(name,email,passwd)
    cursor.execute(query,value)
    conn.commit()
    print("Data insert successfully")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)