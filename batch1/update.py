import mysql.connector

def getconnection():
    host="localhost"
    username="root"
    password=""
    dbname="python_db"
    return mysql.connector.connect(host=host,user=username,password=password,database=dbname)

def update_data(name,age,id):
    conn=getconnection()
    cursor=conn.cursor()
    query="UPDATE users SET name=%s,age=%s WHERE ID = %s"
    cursor.execute(query,(name,age,id))
    conn.commit()
    cursor.close()
    conn.close()
    print("DATA HAS BEEN UPDATED")

update_data("Akash","23","5")