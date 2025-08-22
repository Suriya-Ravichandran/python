# DELETE FROM `product` WHERE `product`.`pid` = 4


import mysql.connector

host="localhost"
user="suriya"
password="suriya@098"
dbname="mydb"
port=3308

try:
    # get values
    # pid=int(input("Enter your product id to delete: "))

    # make database connection
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="SELECT * FROM `product`"
    # values=(pid,)

    # excute the query
    cursor.execute(query)

    # fetch a data
    result=cursor.fetchall()

    for x in result:
        print(x)
    cursor.close()
    conn.close()

except Exception as e:
    print(e)