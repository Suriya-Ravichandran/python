import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch15"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    id=int(input("Enter user id:"))
    cursor=conn.cursor()
    query="SELECT * FROM `user` WHERE id=%s"
    value=(id,)
    cursor.execute(query,value)
    results=cursor.fetchone()
    # for x in results:
    #     print(x)
    print(results)
except Exception as e:
    print(e)