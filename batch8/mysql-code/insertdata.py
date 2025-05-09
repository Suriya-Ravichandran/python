import mysql.connector



host="localhost"
user="root"
password=""
dbname="bank"
port=3307

conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)

name=str(input("Enter username: "))
email=str(input("Enter Email: "))
passwd=str(input("Enter password: "))

cursor=conn.cursor()
query="INSERT INTO `user` (`name`, `email`, `password`) VALUES (%s, %s, %s);"
data=(name,email,passwd)
cursor.execute(query,data)
conn.commit()
print("Insert successfully")
conn.close()
