import mysql.connector

host="localhost"
user="root"
password=""
port=3307
dbname="batch9"

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    print("connection sucessfull")
except Exception as e:
    print(f"Error: {e}")
