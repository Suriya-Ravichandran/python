# CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))

import mysql.connector

host="localhost"
uname="root"
passwd=""
dbname="bank"

conn=mysql.connector.connect(host=host,user=uname,password=passwd,database=dbname)
cursor=conn.cursor()

sql="CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
# val=(5000,"boo")

cursor.execute(sql)
conn.commit()
print("new table created successfully")
conn.close()