import mysql.connector

host="localhost"
uname="root"
passwd=""
dbname="bank"

conn=mysql.connector.connect(host=host,user=uname,password=passwd,database=dbname)
cursor=conn.cursor()

sql="SELECT * FROM user WHERE name=%s"
val=("foo",)
cursor.execute(sql,val)
data=cursor.fetchall()

for x in data:
    print(x)