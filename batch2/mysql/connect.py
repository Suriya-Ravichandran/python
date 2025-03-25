import mysql.connector

host="localhost"
user="root"
password=""
db="deepak"

conn=mysql.connector.connect(host=host,user=user,password=password,database=db)
if(conn):
    print("connection successfull")
else:
    print("Connection failed")