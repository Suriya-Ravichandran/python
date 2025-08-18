import mysql.connector

host="localhost"
user="root"
password="root"
dbname="batch21"
port=3306

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    print("connection sucesss")
except Exception as e:
    print(e)