import mysql.connector
from tabulate import tabulate

def dbconnection():
    hostname="localhost"
    uname="root"
    password=""
    dbname="suriya"
    return mysql.connector.connect(host=hostname,user=uname,password=password,database=dbname)

def getuserdata():
    db=dbconnection()
    cursor=db.cursor()
    query="select * from pyhon"
    cursor.execute(query)
    result=cursor.fetchall()
    headers=["id","name","email","dept"]
    data=[]
    for row in range(len(result)):
        getdata=list(result[row])
        data.append(getdata)

    table=tabulate(data,headers,tablefmt="grid")
    print(table)
    db.commit()
    db.close()

def setuserdata(name,email,dept):
    db=dbconnection()
    cursor=db.cursor()
    query="INSERT INTO pyhon (name, email,department) VALUES (%s, %s,%s)"
    data=(name,email,dept)
    cursor.execute(query,data)
    db.commit()
    db.close()
    return "Add successfully"
def edituserdata(name,dept,email):
     db=dbconnection()
     cursor=db.cursor()
     query="UPDATE pyhon SET name = %s,department= %s WHERE email = %s"
     data=(name,dept,email)
     cursor.execute(query,data)
     db.commit()
     db.close()
     return "update successfully"

def deleteuserdata(email):
     db=dbconnection()
     cursor=db.cursor()
     query="DELETE FROM pyhon WHERE email= %s"
     data=(email,)
     cursor.execute(query,data)
     db.commit()
     db.close()
     return "delete successfully"


