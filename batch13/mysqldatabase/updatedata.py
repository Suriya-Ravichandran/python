import mysql.connector

host="localhost"
user="root"
password=""
database="batch13"
port="3307"
try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)
    id=int(input("Enter update id:"))
    name=str(input("Enter name:"))
    email=str(input("Enter email:"))
    passwd=str(input("Enter password:"))
    cursor=conn.cursor()
    query="UPDATE `user` SET `name` = %s, `email` = %s, `password` = %s WHERE `user`.`id` = %s;"
    value=(name,email,passwd,id)
    cursor.execute(query,value)
    conn.commit()
    conn.close()
    print("Data update successfully")

except Exception as e:
    print(f"Error: {e}")