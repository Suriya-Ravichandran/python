import mysql.connector

host="localhost"
user="root"
password=""
dbname="umarani"

conn = mysql.connector.connect(host=host,user=user,password=password,database=dbname)

name=str(input("Enter Name: "))
email=str(input("Enter Email: "))
passwd=str(input("Enter Password: "))
address=str(input("Enter Addess: "))

cursor=conn.cursor()
query="INSERT INTO `user` (`name`, `email`, `password`, `address`) VALUES (%s,%s,%s,%s);"
val=(name,email,passwd,address)
cursor.execute(query,val)
conn.commit()
print("Insert data successfully")
