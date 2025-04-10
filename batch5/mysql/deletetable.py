import mysql.connector

host="localhost"
user="root"
password=""
dbname="dhanapriya"

con=mysql.connector.connect(host=host,user=user,password=password,database=dbname)


cursor=con.cursor()
query="DROP TABLE student;"

cursor.execute(query)
con.commit()
print("Delete Table successfull")