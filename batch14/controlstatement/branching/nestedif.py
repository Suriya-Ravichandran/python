email="foo@gmail.com"
password="foo@123"
useremail=str(input("Enter username:"))
userpassword=str(input("Enter password:"))

if email==useremail:
    if password==userpassword:
        print("Login success")
    else:
        print("Incorrect password")
else:
    print("user not found")