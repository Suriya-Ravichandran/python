import mysql.connector

host="localhost"
user="root"
password=""
dbname="dhanapriya"

con=mysql.connector.connect(host=host,user=user,password=password,database=dbname)

cursor=con.cursor()
query="SELECT * FROM STUDENT"
cursor.execute(query)
result=cursor.fetchall()

for x in result:
    print(x)