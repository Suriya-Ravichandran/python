import mysql.connector

host="localhost"
user="root"
password=""
database="batch13"
port="3307"
try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)
    name=str(input("Enter name:"))
    email=str(input("Enter email:"))
    passwd=str(input("Enter password:"))
    cursor=conn.cursor()
    query="INSERT INTO `user` (`name`, `email`, `password`) VALUES (%s, %s, %s);"
    value=(name,email,passwd)
    cursor.execute(query,value)
    conn.commit()
    conn.close()
    print("Data insert successfully")

except Exception as e:
    print(f"Error: {e}")