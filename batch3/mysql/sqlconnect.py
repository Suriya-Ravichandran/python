import mysql.connector

host="localhost"
uname="root"
passwd=""
dbname="bank"

conn=mysql.connector.connect(host=host,user=uname,password=passwd,database=dbname)
cursor=conn.cursor()

sql="SELECT * FROM USER"

cursor.execute(sql)
data=cursor.fetchall()

for x in data:
    print(x)