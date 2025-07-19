import mysql.connector

host="localhost"
user="root"
password=""
dbname="demo"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)

    email=str(input("Enter email: "))
    passwd=str(input("Enter your password: "))


    cursor=conn.cursor()
    value=(email,)
    query="SELECT * FROM `user` WHERE email=%s"
    cursor.execute(query,value)
    result=cursor.fetchone()
    if result==None:
        print("User not found")
    else:
        (id,name,email,verifypassword)=result
        if passwd==verifypassword:
            print("Login success")
        else:
            print("incorrect password")

    cursor.close()
    conn.close()
except Exception as e:
    print(e)