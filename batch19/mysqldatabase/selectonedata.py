import mysql.connector


host="localhost"
user="root"
password=""
dbname="batch19"
port=3307


try:
    pid=int(input("Enter Product id: "))
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="SELECT * FROM `product` WHERE `id`=%s"
    values=(pid,)
    cursor.execute(query,values)
    result=cursor.fetchone()
    print(result)
    conn.close()
except Exception as e:
    print(e)