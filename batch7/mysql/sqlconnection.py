import mysql.connector

host="localhost"
usr="root"
passwd=""
db_name="student"

try:
    conn=mysql.connector.connect(host=host,user=usr,password=passwd,database=db_name)
    if(conn):
         print("connection success")
    else:
        print("connection failed")
except:
    print("database is inactive")


