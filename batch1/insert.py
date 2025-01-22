import mysql.connector

def getconnection():
    host="localhost"
    username="root"
    password=""
    dbname="python_db"
    return mysql.connector.connect(host=host,user=username,password=password,database=dbname)

def insert_data(name,age):
    conn=getconnection()
    cursor=conn.cursor()
    query="INSERT INTO users(name,age) VALUES(%s,%s)"
    cursor.execute(query,(name,age))
    conn.commit()
    cursor.close()
    conn.close()
    print("DATA HAS BEEN INSERTED")

insert_data("AKASH","23")