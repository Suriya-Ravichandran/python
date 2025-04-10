import mysql.connector

host="localhost"
user="root"
password=""
dbname="dhanapriya"

con=mysql.connector.connect(host=host,user=user,password=password,database=dbname)

id=str(input("Enter id: "))
cursor=con.cursor()
query="DELETE FROM `student` WHERE `student`.`sid` = %s"
val=(id,)
cursor.execute(query,val)
con.commit()
print("delete data successfull")