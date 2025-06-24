import mysql.connector

hostname="localhost"
user="root"
password=""
dbname="batch14"
port=3307

try:
    conn=mysql.connector.connect(host=hostname,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    id=int(input("Enter yours id: "))
    passwd=str(input("Enter your password: "))
    query="SELECT * FROM `user` WHERE id=%s"
    value=(id,)
    cursor.execute(query,value)
    result=cursor.fetchone()
    (id,name,email,password)=result
    if passwd==password:
        print("login success")
    else:
        print("incorrect password")

    cursor.close()
    conn.close()
except Exception as e:
    print(e)