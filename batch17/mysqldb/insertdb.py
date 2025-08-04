import mysql.connector

host=""
user=""
password=""
dbname=""
port=3306

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()

    name=str(input("Enter your name: "))
    email=str(input("Enter your email: "))
    passwd=str(input("Enter your password: "))

    value=(name,email,passwd)
    query="INSERT INTO `user` (`name`, `email`, `password`) VALUES (%s, %s, %s);"
    cursor.execute(query,value)
    conn.commit()
    print("Insert successfully")
    conn.close()
except Exception as e:
    print(f"Error: {e}")