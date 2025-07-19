import mysql.connector

host="localhost"
user="root"
password=""
dbname="demo"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    name=str(input("Enter name: "))
    email=str(input("Enter email: "))
    passwd=str(input("Enter password: "))
    cursor=conn.cursor()
    value=(name,email,passwd)
    query="INSERT INTO `user` (`name`, `email`, `password`) VALUES (%s,%s, %s);"
    cursor.execute(query,value)
    conn.commit()
    print("insert data sucessfully")
    cursor.close()
    conn.close()
except Exception as e:
    print(e)


    