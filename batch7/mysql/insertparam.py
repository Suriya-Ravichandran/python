import mysql.connector

host = "localhost"
usr = "root"
passwd = ""
db_name = "student"

conn = mysql.connector.connect(host=host, user=usr, password=passwd, database=db_name)

name=str(input("Enter name: "))
dob=str(input("Enter DOB: "))
dept=str(input("Enter Dept: "))


cursor = conn.cursor()
query = "INSERT INTO user (`name`, `dataofbirth`, `dept`) VALUES (%s, %s, %s)"
val=(name,dob,dept)
cursor.execute(query,val)
conn.commit()
print("data added success fully")
cursor.close()
conn.close()