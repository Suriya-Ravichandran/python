import mysql.connector


host="localhost"
user="root"
password=""
dbname="batch19"
port=3307


try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    print("Connection success")
except Exception as e:
    print(e)