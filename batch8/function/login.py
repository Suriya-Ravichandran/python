
def login(email,password): 
    verifypassword="suriya@123"
    verifyemail="rsuriya@gmail.com"
    if email==verifyemail:
        if password==verifypassword:
            return "login success"
        else:
            return "Password incorrect"
    else:
        return "User Not found"
    

while True:
    email=str(input("Enter your Email: "))
    password=str(input("Enter your Password: "))
    message=login(email,password)
    print(message)
    if message == "login success":
        break
