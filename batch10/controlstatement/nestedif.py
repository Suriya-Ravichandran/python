verfiyusername="foo@gmail.com"
verfiypassword="foo@123"

username=str(input("Enter your Username: "))
password=str(input("Enter your Password: "))

if username==verfiyusername:
    if password==verfiypassword:
        print("Login successs")
    else:
        print("Incorrect Password")
else:
    print("User not found !!!")

 