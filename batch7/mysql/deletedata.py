import mysql.connector

host = "localhost"
usr = "root"
passwd = ""
db_name = "student"

conn = mysql.connector.connect(host=host, user=usr, password=passwd, database=db_name)

cursor = conn.cursor()
query = "DELETE FROM `user` WHERE `id` = %s"
val=(8,)
cursor.execute(query,val)

conn.commit()
print("data delete successfully")
cursor.close()
conn.close()