import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch11"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="SELECT * FROM `user`"
    cursor.execute(query)
    result=cursor.fetchall()
    for x in result:
        print(x)
    conn.close()

except Exception as e:
    print(f"Error: {e}")