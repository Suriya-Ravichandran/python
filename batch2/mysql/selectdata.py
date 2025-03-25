import mysql.connector

host="localhost"
user="root"
password=""
db="deepak"

conn=mysql.connector.connect(host=host,user=user,password=password,database=db)

cursor=conn.cursor()

sql="SELECT * FROM student"

cursor.execute(sql)
data=cursor.fetchall()
for x in data:
    print(x)

conn.close()
