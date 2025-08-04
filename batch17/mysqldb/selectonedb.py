
import mysql.connector

host=""
user=""
password=""
dbname=""
port=3306

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    useremail=str(input("Enter user email: "))
    passwd=str(input("Enter password: "))
    value=(useremail,)
    query="SELECT * FROM `user` WHERE `email`=%s;"
    cursor.execute(query,value)
    result=cursor.fetchone()
    if result!=None:
        (userid,name,email,passwd1,)=result
        if useremail==email:
            if passwd==passwd1:
                print(f"Welcome {name}")
            else:
                print("incorrect password")
        else:
            print("User not found")
    else:
            print("User not found")

    conn.close()
except Exception as e:
    print(f"Error: {e}")