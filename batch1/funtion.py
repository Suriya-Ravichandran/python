import mysql.connector
from mysql.connector import Error

def dbconnect(hostname, username, password, dbname):
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
            database=dbname
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

# Test the connection
connection = dbconnect(hostname="localhost", username="root", password="", dbname="python_db")
if connection:
    print("Connection success")
    connection.close()  # Close the connection when done
else:
    print("Connection refused")
