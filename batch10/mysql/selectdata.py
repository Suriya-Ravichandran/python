# SELECT * FROM `user`

import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch10"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    # print("Connection Sucessfully")

    id=int(input("Enter user id to select: "))

    cursor=conn.cursor()


    query="SELECT * FROM `user` WHERE id=%s"
    val=(id,)
    cursor.execute(query,val)
    result = cursor.fetchall()

    for results in result:
        print(results) 

    conn.close()


except Exception as e:
    print(f"Error: {e}")