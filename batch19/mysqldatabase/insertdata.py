import mysql.connector


host="localhost"
user="root"
password=""
dbname="batch19"
port=3307


try:
    productname=str(input("Enter Product name: "))
    productdescription=str(input("Enter Product Description: "))
    quantity=int(input("Enter quantity: "))

    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="INSERT INTO `product` (`productname`, `description`, `quantity`) VALUES (%s, %s, %s);"
    values=(productname,productdescription,quantity)
    cursor.execute(query,values)
    print("Data insert success")
    conn.commit()
    conn.close()
except Exception as e:
    print(e)