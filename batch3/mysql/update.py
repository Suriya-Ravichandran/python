import mysql.connector

host="localhost"
uname="root"
passwd=""
dbname="bank"

conn=mysql.connector.connect(host=host,user=uname,password=passwd,database=dbname)
cursor=conn.cursor()

sql="UPDATE user SET balance=%s WHERE NAME=%s"
val=(5000,"boo")

cursor.execute(sql,val)
conn.commit()
print("data update successfully")
conn.close()