import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch10"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    print("Connection Sucessfully")
except Exception as e:
    print(f"Error: {e}")