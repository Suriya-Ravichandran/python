import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch10"
port=3307

conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)

if conn:
    print("Connection Sucessfully")