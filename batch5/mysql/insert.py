import mysql.connector

host="localhost"
user="root"
password=""
dbname="dhanapriya"

con=mysql.connector.connect(host=host,user=user,password=password,database=dbname)

name=str(input("Enter name: "))
dob=str(input("Enter Dob: "))
department=str(input("Enter Department: "))
cursor=con.cursor()
query="INSERT INTO `student` (`name`, `dateofbirth`, `department`) VALUES (%s,%s,%s);"
val=(name,dob,department)
cursor.execute(query,val)
con.commit()
print("Insert data successfull")