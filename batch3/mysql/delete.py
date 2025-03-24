import mysql.connector

host="localhost"
uname="root"
passwd=""
dbname="bank"

conn=mysql.connector.connect(host=host,user=uname,password=passwd,database=dbname)
cursor=conn.cursor()

sql="DELETE FROM user WHERE NAME=%s"
val=("boo",)

cursor.execute(sql,val)
conn.commit()
print("data Deteted successfully")
conn.close()