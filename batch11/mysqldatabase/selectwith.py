import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch11"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    email=str(input("Enter user email: "))
    cursor=conn.cursor()
    query="SELECT * FROM `user` WHERE `email`=%s"
    value=(email,)
    cursor.execute(query,value)
    result=cursor.fetchone()
    (id,name,email,password)=result
    print(name)
    conn.close()

except Exception as e:
    print(f"Error: {e}")