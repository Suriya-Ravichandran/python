import mysql.connector

host="localhost"
user="root"
password=""
port=3307
dbname="batch9"

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="SELECT * FROM USER;"
    cursor.execute(query)
    result=cursor.fetchall()

    for x in result:
        print(x)
    
    conn.close()

except Exception as e:
    print(f"Error: {e}")