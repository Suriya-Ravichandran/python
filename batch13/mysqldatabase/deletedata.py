import mysql.connector

host="localhost"
user="root"
password=""
database="batch13"
port="3307"
try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)
    id=str(input("Enter Id to Delete:"))
    cursor=conn.cursor()
    query="DELETE FROM `user` WHERE `user`.`id` = %s"
    value=(id,)
    cursor.execute(query,value)
    conn.commit()
    conn.close()
    print("Data delete successfully")

except Exception as e:
    print(f"Error: {e}")