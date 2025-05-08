import mysql.connector


host="localhost"
user="root"
password=""
dbname="batch7"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    print("Connection successfully")
    refers=conn.cursor()
    query="INSERT INTO `user` (`name`, `email`, `password`, `age`) VALUES ( %s, %s, %s, %s);"
    values=("koo","koo@gmail.com","koo@123",23)
    refers.execute(query,values)
    print("Insert Data success")
    conn.commit()
    conn.close()
except mysql.connector.errors.DatabaseError:
    print("Connection failed")