import mysql.connector

host="localhost"
user="root"
password=""
database="batch12"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)
    cursor=conn.cursor()
    query="INSERT INTO `user` (`name`, `email`, `password`) VALUES ('zoo', 'zoo@gmail.com', 'zoo@123');"
    cursor.execute(query)
    print("Data insert succesfully")
    conn.commit()
    conn.close()
except Exception as e:
    print(e)