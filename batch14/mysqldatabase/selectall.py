import mysql.connector

hostname="localhost"
user="root"
password=""
dbname="batch14"
port=3307

try:
    conn=mysql.connector.connect(host=hostname,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="SELECT * FROM `user`"
    cursor.execute(query)
    result=cursor.fetchall()
    for results in result:
        print(results)
    cursor.close()
    conn.close()
except Exception as e:
    print(e)