print("---------Login system app-----------")
verfiyuser="foo"
verfiypass="foo@123"

username=str(input("Enter your username: "))
password=str(input("Enter your password: "))

if username==verfiyuser:
    if password==verfiypass:
        print("Login success !!")
    else:
        print("Invaild password")
else:
    print("User not found")