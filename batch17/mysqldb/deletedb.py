



import mysql.connector

host=""
user=""
password=""
dbname=""
port=3306

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()

    userid=int(input("Enter update user id: "))

    value=(userid,)
    query="DELETE FROM `user` WHERE `id` = %s;"
    cursor.execute(query,value)
    conn.commit()
    print("delete successfully")
    conn.close()
except Exception as e:
    print(f"Error: {e}")