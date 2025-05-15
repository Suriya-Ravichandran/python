import numpy as np
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
result=cursor.fetchone()
data=[]
for results in result:
    data.append(results)
conn.close()

data=np.array(data)
print(type(data))
print(data)
