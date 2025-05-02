while True:
    username=str(input("Enter username: "))
    password=str(input("Enter Password: "))
    verifyuser="suriya"
    verifypass="suriya@123"
    if username==verifyuser:
        if password==verifypass:
            print("Login success")
            break
        else:
            print("Incorrect password")
    else:
        print("User not found")
        

