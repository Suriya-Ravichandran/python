import mysql.connector

host="localhost"
user="suriya"
password="suriya@098"
dbname="mydb"
port=3308

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    print("connection sucesss")
except Exception as e:
    print(e)