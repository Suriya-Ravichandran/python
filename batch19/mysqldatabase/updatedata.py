

import mysql.connector


host="localhost"
user="root"
password=""
dbname="batch19"
port=3307


try:
    pid=int(input("Enter product id to update: "))
    productname=str(input("Enter Product name: "))
    productdescription=str(input("Enter Product Description: "))
    quantity=int(input("Enter quantity: "))

    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="UPDATE `product` SET `productname` = %s, `description` = %s,`quantity`=%s WHERE `product`.`id` = %s;"
    values=(productname,productdescription,quantity,pid)
    cursor.execute(query,values)
    print("Data update success")
    conn.commit()
    conn.close()
except Exception as e:
    print(e)