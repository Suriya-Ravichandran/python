import mysql.connector

host="localhost"
user="root"
password=""
db="deepak"

conn=mysql.connector.connect(host=host,user=user,password=password,database=db)

cursor=conn.cursor()

sql="INSERT INTO student (name,dateofbirth,tamil,english,maths,science,social) VALUES(%s,%s,%s,%s,%s,%s,%s)"
val=("foo","12-1-2007",78,80,60,65,70)
cursor.execute(sql,val)
print("data insert success")
conn.commit()
conn.close()
