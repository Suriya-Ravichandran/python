import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch15"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="SELECT * FROM `user`"
    cursor.execute(query)
    results=cursor.fetchall()
    for x in results:
        print(x)
except Exception as e:
    print(e)