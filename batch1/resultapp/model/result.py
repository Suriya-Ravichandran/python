import mysql.connector
from tabulate import tabulate

def getconnection():
    host="localhost"
    username="root"
    password=""
    db="student"
    return mysql.connector.connect(host=host,user=username,password=password,database=db)

def getresult(id):
    db=getconnection()
    cursor=db.cursor()
    query=f"SELECT * FROM result WHERE id={id}"
    # studentdata=[id,dob]
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
    db.commit()
    db.close()