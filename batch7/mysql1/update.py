# SELECT * FROM `user`
# INSERT INTO `user` (`id`, `name`, `email`, `password`, `age`) VALUES ('1', 'foo', 'foo@gmail.com', 'foo@123', '23');
# UPDATE `user` SET `name` = 'zoo', `email` = 'zoo@gmail.com', `password` = 'zoo@123' WHERE `user`.`id` = 4;
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
    query=" UPDATE `user` SET `name` = %s, `email` = %s, `password` = %s WHERE `user`.`id` =%s;"
    values=("koo","koo@gmail.com","koo@123",1)
    refers.execute(query,values)
    print("Update Data success")
    conn.commit()
    conn.close()
except mysql.connector.errors.DatabaseError:
    print("Connection failed")