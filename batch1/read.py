import mysql.connector

def getconnection():
    host="localhost"
    username="root"
    password=""
    dbname="python_db"
    return mysql.connector.connect(host=host,user=username,password=password,database=dbname)

def read_data():
    conn=getconnection()
    conn=getconnection()
    cursor=conn.cursor()
    query="SELECT * FROM users"
    cursor.execute(query)
    result=cursor.fetchall()
    for results in result:
        print(results)
    cursor.close()
    conn.close()
read_data()