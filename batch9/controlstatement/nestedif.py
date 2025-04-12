verifyuser="suriya"
verifypassword="suriya@123"

username=str(input("Enter username: "))
password=str(input("Enter password: "))

if(username==verifyuser):
    if(password==verifypassword):
        print("Login success")
    else:
        print("Incorrect password !!")
        
else:
    print("User Not found")