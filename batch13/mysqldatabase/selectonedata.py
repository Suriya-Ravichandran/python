import mysql.connector

host="localhost"
user="root"
password=""
database="batch13"
port="3307"
try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)
    id=int(input("Enter id:"))
    cursor=conn.cursor()
    query="SELECT * FROM user WHERE id=%s"
    value=(id,)
    cursor.execute(query,value)
    results=cursor.fetchone()
    # for result in results:
    print(results)
    (userid,username,useremail,userpassword)=results
    print(userpassword)
    conn.close()

except Exception as e:
    print(f"Error: {e}")