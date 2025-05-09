import mysql.connector



host="localhost"
user="root"
password=""
dbname="bank"
port=3307

conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)

cursor=conn.cursor()
query="SELECT * FROM `user` WHERE id=1;"
cursor.execute(query)
result=cursor.fetchall()
# data=[]
data=()
for results in result:
    data=results

(id,name,email,passwd)=data

print("Name:",name)
conn.close()
