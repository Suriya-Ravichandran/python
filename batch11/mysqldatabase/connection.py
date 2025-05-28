import mysql.connector

host="localhost"
user="root"
password=""
dbname="batch11"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=dbname,port=port)
    print("Connection success")
except Exception as e:
    print(f"Error: {e}")


# SELECT * FROM `user`
# INSERT INTO `user` (`id`, `name`, `email`, `password`) VALUES ('1', 'foo', 'foo@gmail.com', 'foo@123');
# UPDATE `user` SET `name` = 'hoo', `email` = 'hoo@gmail.com', `password` = 'hoo@123' WHERE `user`.`id` = 3;
# DELETE FROM `user` WHERE `user`.`id` = 2