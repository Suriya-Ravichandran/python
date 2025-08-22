# UPDATE `product` SET `productname` = 'goa', `description` = 'this a green goa', `quantity` = '10' WHERE `product`.`pid` = 2;


import mysql.connector

host="localhost"
user="suriya"
password="suriya@098"
dbname="mydb"
port=3308

try:
    # get values
    pid=int(input("Enter your product id to update: "))
    productname=str(input("Enter product name: "))
    description=str(input("Enter product description: "))
    quantity=int(input("Enter product quantity: "))

    # make database connection
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="UPDATE `product` SET `productname` = %s, `description` = %s, `quantity` = %s WHERE `product`.`pid` =%s;"
    values=(productname,description,quantity,pid)

    # excute the query
    cursor.execute(query,values)

    # save a data
    conn.commit()
    cursor.close()
    conn.close()
    print("Data update successfully")

except Exception as e:
    print(e)