import mysql.connector

host="localhost"
user="root"
password=""
db="deepak"

conn=mysql.connector.connect(host=host,user=user,password=password,database=db)

cursor=conn.cursor()

sql = "UPDATE student SET name = %s WHERE id = %s"

val=("foo",3)

cursor.execute(sql,val)
print("data update success")
conn.commit()
conn.close()


