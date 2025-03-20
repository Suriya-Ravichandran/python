import mysql.connector

host="localhost"
uname="root"
passwd=""
dbname="bank"



conn=mysql.connector.connect(host=host,user=uname,password=passwd,database=dbname)
if(conn):
    print("conection sucessfully")
