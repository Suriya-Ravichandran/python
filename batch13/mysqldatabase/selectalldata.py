import mysql.connector

host="localhost"
user="root"
password=""
database="batch13"
port="3307"
try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)
    cursor=conn.cursor()
    query="SELECT * FROM `user`"
    cursor.execute(query)
    results=cursor.fetchall()
    for result in results:
        print(result)
    conn.close()

except Exception as e:
    print(f"Error: {e}")