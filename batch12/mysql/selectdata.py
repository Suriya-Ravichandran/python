import mysql.connector

host="localhost"
user="root"
password=""
database="batch12"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)
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