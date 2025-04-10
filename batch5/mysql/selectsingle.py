import mysql.connector

host="localhost"
user="root"
password=""
dbname="dhanapriya"

con=mysql.connector.connect(host=host,user=user,password=password,database=dbname)


id=int(input("Enter id: "))
cursor=con.cursor()
query="SELECT name FROM STUDENT WHERE sid=%s"
val=(id,)
cursor.execute(query,val)
result=cursor.fetchall()

for x in result:
    print(x)
    for j in x:
        print(j)
