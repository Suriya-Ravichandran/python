import mysql.connector


try:
    host="localhost"
    user="root"
    password=""
    dbname="bank"
    port=3307

    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    print("Connection sucessfully")
except Exception as e:
    print(e)