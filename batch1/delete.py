import mysql.connector

def getconnection():
    host="localhost"
    username="root"
    password=""
    dbname="python_db"
    return mysql.connector.connect(host=host,user=username,password=password,database=dbname)

def delete_data(id):
    conn = getconnection()
    cursor = conn.cursor()
    
    # Correct way to pass parameters in the query
    query = "DELETE FROM users WHERE ID = %s"
    
    # Pass 'id' as a tuple
    cursor.execute(query, (id,))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    print("DATA HAS BEEN DELETED")

delete_data(3) 

