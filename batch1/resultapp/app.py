#INSERT INTO `result` (`id`, `name`, `dob`, `tamil`, `computer`, `maths`) VALUES ('1', 'foo', '1-2-2000', '75', '85', '65');

import mysql.connector
from tabulate import tabulate

host="localhost"
username="root"
password=""
db="student"


con=mysql.connector.connect(host=host,user=username,password=password,database=db)
if(con):
    print("connected")
else:
    print("not connected")

cursor=con.cursor()
query="SELECT * FROM result"
cursor.execute(query)
row=cursor.fetchall()
# Column headers
headers = ["id", "name", "dob","tamil","computer","maths"]
data=[]


for result in range(len(row)):
    getdata=row[result]
    data.append(getdata)
table=tabulate(data,headers,tablefmt="grid")
print(table)
con.commit()
con.close()