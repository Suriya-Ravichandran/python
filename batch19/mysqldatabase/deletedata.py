import mysql.connector


host="localhost"
user="root"
password=""
dbname="batch19"
port=3307


try:
    pid=int(input("Enter product id to delete: "))
    
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="DELETE FROM `product` WHERE `product`.`id` = %s"
    values=(pid,)
    cursor.execute(query,values)
    print("Data delete success")
    conn.commit()
    conn.close()
except Exception as e:
    print(e)