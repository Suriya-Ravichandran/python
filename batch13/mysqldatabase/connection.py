import mysql.connector

host="localhost"
user="root"
password=""
database="batch13"
port="3307"


try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)
    print("connection successfully")
except Exception as e:
    print(f"Error: {e}")