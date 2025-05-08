# SELECT * FROM `user`
# INSERT INTO `user` (`id`, `name`, `email`, `password`, `age`) VALUES ('1', 'foo', 'foo@gmail.com', 'foo@123', '23');
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
    query="SELECT * FROM `user`"
    refers.execute(query)
    result=refers.fetchall()
    for x in result:
        print(x)
    conn.close()
    
except mysql.connector.errors.DatabaseError:
    print("Connection failed")