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

def update_data(name,age,id):
    conn=getconnection()
    cursor=conn.cursor()
    query="UPDATE users SET name=%s,age=%s WHERE ID = %s"
    cursor.execute(query,(name,age,id))
    conn.commit()
    cursor.close()
    conn.close()
    print("DATA HAS BEEN UPDATED")

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

print("TO INSERT 1,TO UPDATE 2,TO READ 3,TO DELETE 4")

opition=int(input("Enter your choice"))
if(opition==1):
    name=str(input("Enter Name"))
    age=str(input("Enter age"))
    insert_data(name,age)
elif(opition==2):
    id=int(input("Enter id "))
    name=str(input("Enter Name"))
    age=str(input("Enter Age"))
    update_data(name,age,id)
elif(opition==3):
    read_data()
elif(opition==4):
    id=int(input("Enter id"))
    delete_data(id)
else:
    print("invaild option")

    

