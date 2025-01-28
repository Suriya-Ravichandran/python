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


def getallresult():
    db=getconnection()
    cursor=db.cursor()
    query="SELECT * FROM result"
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


def addresult(id, name, dob, tamil, computer, maths):
    db = getconnection()
    cursor = db.cursor()
    query = "INSERT INTO result (id, name, dob, tamil, computer, maths) VALUES (%s, %s, %s, %s, %s, %s)"
    resultdata = (id, name, dob, tamil, computer, maths)
    try:
        cursor.execute(query, resultdata)
        db.commit()
        print("Data inserted successfully")
    except Exception as e:
        print("Data Insert failed")
    finally:
        db.close()

def updateresult(name, dob, tamil, computer, maths,id):
    db = getconnection()
    cursor = db.cursor()
    query = "UPDATE result SET name = %s,dob=%s,tamil=%s,computer=%s,maths=%s WHERE id = %s"
    resultdata = (name, dob, tamil, computer, maths,id)
    try:
        cursor.execute(query, resultdata)
        db.commit()
        print("Data Update successfully")
    except Exception as e:
        print("Data Insert failed")
    finally:
        db.close()


def Deleteresult(id):
    db = getconnection()
    cursor = db.cursor()
    query = "DELETE FROM result WHERE id = %s"
    resultdata = (id,)
    try:
        cursor.execute(query, resultdata)
        db.commit()
        print("Data Deleted successfully")
    except Exception as e:
        print("Data Insert failed")
    finally:
        db.close()
