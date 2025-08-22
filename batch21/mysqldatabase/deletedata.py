# DELETE FROM `product` WHERE `product`.`pid` = 4


import mysql.connector

host="localhost"
user="suriya"
password="suriya@098"
dbname="mydb"
port=3308

try:
    # get values
    pid=int(input("Enter your product id to delete: "))

    # make database connection
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    cursor=conn.cursor()
    query="DELETE FROM `product` WHERE `product`.`pid` = %s"
    values=(pid,)

    # excute the query
    cursor.execute(query,values)

    # save a data
    conn.commit()
    cursor.close()
    conn.close()
    print("Data delete successfully")

except Exception as e:
    print(e)