import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch11"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    name=str(input("Enter username: "))
    email=str(input("Enter user email: "))
    password=str(input("Enter password: "))
    cursor=conn.cursor()
    query="INSERT INTO `user` (`name`, `email`, `password`) VALUES (%s, %s,%s);"
    value=(name,email,password)
    cursor.execute(query,value)
    conn.commit()
    conn.close()
    print("Data insert sucessfully")

except Exception as e:
    print(f"Error: {e}")