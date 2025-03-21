import mysql.connector

host="localhost"
usr="root"
passwd=""
db_name="student"

try:
    conn=mysql.connector.connect(host=host,user=usr,password=passwd,database=db_name)
    # if(conn):
    #      print("connection success")
    # else:
    #     print("connection failed")
    cursor=conn.cursor()
    query="INSERT INTO user values(%s,%s,%s,%s)"
    value=(2,"foo","1-1-2025","BCA")
    if(cursor.execute(query,value)):
        conn.commit()
        conn.close()
        print("data inserted")
    else:
        print("Insert failed")
except:
    print("database is inactive")