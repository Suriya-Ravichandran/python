import mysql.connector

host="localhost"
user="root"
password=""
database="batch12"
port=3307

try:
    conn=mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)
    print("Sucessfully connected")
except Exception as e:
    print(e)


# INSERT INTO `user` (`id`, `name`, `email`, `password`) VALUES ('1', 'foo', 'foo@gmail.com', 'foo@123');

