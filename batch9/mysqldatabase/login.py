import mysql.connector

host = "localhost"
user = "root"
password = ""
dbname = "batch9"
port = 3307

try:
    # Establish database connection
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=dbname,
        port=port
    )
    
    email = input("Enter User Email: ").strip()
    
    cursor = conn.cursor()
    query = "SELECT `password[` FROM `user` WHERE `email` = %s;"
    cursor.execute(query, (email,))
    
    result = cursor.fetchone()
    
    if result:
        user_password = result[0]
        password=str(input("Enter your password: "))
        if user_password==password:
            print("Login success")
    else:
        print("No user found with that email.")

    conn.close()

except mysql.connector.Error as db_err:
    print(f"Database error: {db_err}")
except Exception as e:
    print(f"An error occurred: {e}")
