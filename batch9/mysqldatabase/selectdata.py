import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch9"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    id=int(input("Enter id to select user: "))
    # print("Connection successfull")
    cursor=conn.cursor()
    query="SELECT * FROM `user` WHERE id=%s;"
    values=(id,)
    cursor.execute(query,values)
    result=cursor.fetchall()
    for results in result:
        print(results)
    conn.close()

except Exception as e:
    print(f"Error: {e}")