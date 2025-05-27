import mysql.connector

host="localhost"
user="root"
password=""
port=3307
dbname="batch9"

try:
    email=str(input("Enter Email: "))
    passwd1=str(input("Enter password: "))
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="SELECT * FROM user WHERE email = %s"
    value=(email,)
    cursor.execute(query,value)
    result=cursor.fetchone()
    # for x in result:
    #     print(x)
    
    (id,user,email,passwd2)=result
    if passwd1==passwd2:
        print("Login success")
    else:
        print("login failed")



    conn.close()



except Exception as e:
    print(f"Error: {e}")