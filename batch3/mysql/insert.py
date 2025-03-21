import mysql.connector

host="localhost"
uname="root"
passwd=""
dbname="bank"

conn=mysql.connector.connect(host=host,user=uname,password=passwd,database=dbname)
cursor=conn.cursor()

sql="INSERT INTO user (name,acc_type,balance)VALUES(%s,%s,%s)"
val=("boo","current",2000)

cursor.execute(sql,val)
conn.commit()
print("data insert successfully")
conn.close()