import mysql.connector

host = "localhost"
usr = "root"
passwd = ""
db_name = "student"

conn = mysql.connector.connect(host=host, user=usr, password=passwd, database=db_name)
cursor = conn.cursor()
query = "SELECT * FROM user"
cursor.execute(query)
result = cursor.fetchall()
for x in result:
    print(x)

cursor.close()
conn.close()



