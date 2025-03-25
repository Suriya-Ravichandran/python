import mysql.connector

host="localhost"
user="root"
password=""
db="deepak"

conn=mysql.connector.connect(host=host,user=user,password=password,database=db)

cursor=conn.cursor()

sql="DELETE FROM student WHERE id=%s"
val=(4,)

cursor.execute(sql,val)
print("data delete success")
conn.commit()
conn.close()
