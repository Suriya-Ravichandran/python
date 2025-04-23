import mysql.connector

host="localhost"
user="root"
password=""
dbname="umarani"

conn = mysql.connector.connect(host=host,user=user,password=password,database=dbname)

cursor=conn.cursor()

query="SELECT * FROM USER;"
cursor.execute(query)
result=cursor.fetchall()

for x in result:
    print(x)
