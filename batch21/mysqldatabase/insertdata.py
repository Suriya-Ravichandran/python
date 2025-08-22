# INSERT INTO `product` (`pid`, `productname`, `description`, `quantity`) VALUES ('1', 'apple', 'this a red apple', '100');


import mysql.connector

host="localhost"
user="suriya"
password="suriya@098"
dbname="mydb"
port=3308

try:
    # get values
    productname=str(input("Enter product name: "))
    description=str(input("Enter product description: "))
    quantity=int(input("Enter product quantity: "))

    # make database connection
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="INSERT INTO `product` (`productname`, `description`, `quantity`) VALUES (%s, %s, %s);"
    values=(productname,description,quantity)

    # excute the query
    cursor.execute(query,values)

    # save a data
    conn.commit()
    cursor.close()
    conn.close()
    print("Data insert successfully")

except Exception as e:
    print(e)