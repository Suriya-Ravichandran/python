import mysql.connector

host = "localhost"
usr = "root"
passwd = ""
db_name = "student"

conn = mysql.connector.connect(host=host, user=usr, password=passwd, database=db_name)

cursor = conn.cursor()
query = "UPDATE `user` SET `name` = %s WHERE `id` = %s"
val=("suriya",10)
cursor.execute(query,val)

conn.commit()
print("data update successfully")
cursor.close()
conn.close()