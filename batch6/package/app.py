from user.auth import auth



while True:
    print("1 to sign\n2 to login")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        name=str(input("Enter username: "))
        password=str(input("Enter passwd: "))
        u1=auth(name,password)
    elif(choice==2):
        name=str(input("Enter username: "))
        password=str(input("Enter passwd: "))
        verifypassword=u1.getpassword
        print(verifypassword)
        u1.login(verifypassword,password)
    else:
        break