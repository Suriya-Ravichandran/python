import mysql.connector

hostname="localhost"
uname="root"
password=""
dbname="suriya"
con=mysql.connector.connect(host=hostname,user=uname,password=password,database=dbname)
cursor=con.cursor()

query="select * from pyhon"
cursor.execute(query)
result=cursor.fetchall()
for row in result:
    print(row)
con.commit()
con.close()
