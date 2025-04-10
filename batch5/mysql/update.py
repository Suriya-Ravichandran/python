import mysql.connector

host="localhost"
user="root"
password=""
dbname="dhanapriya"

con=mysql.connector.connect(host=host,user=user,password=password,database=dbname)

id=str(input("Enter id: "))
name=str(input("Enter name: "))
cursor=con.cursor()
query="UPDATE `student` SET `name` = %s WHERE `student`.`sid` = %s;"
val=(name,id)
cursor.execute(query,val)
con.commit()
print("update data successfull")