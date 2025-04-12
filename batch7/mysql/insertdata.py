import mysql.connector

host = "localhost"
usr = "root"
passwd = ""
db_name = "student"

conn = mysql.connector.connect(host=host, user=usr, password=passwd, database=db_name)

cursor = conn.cursor()
query = "INSERT INTO user (`name`, `dataofbirth`, `dept`) VALUES ('hoo', '12-12-2002', 'MBA')"
cursor.execute(query)
conn.commit()
print("data added success fully")
cursor.close()
conn.close()