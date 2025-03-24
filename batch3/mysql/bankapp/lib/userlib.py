import mysql.connector
def connect():
    host="localhost"
    uname="root"
    passwd=""
    dbname="bank"
    connect=mysql.connector.connect(host=host,user=uname,password=passwd,database=dbname)
    return connect

def signup(name,email,phone,addess,password,account_type,intial_balance=0.0):
    conn=connect()

    pass

def login():
    pass

def editprofile():
    pass

def creditamount():
    pass

def debitamount():
    pass

def deleteaccount():
    pass

def tranferamount():
    pass