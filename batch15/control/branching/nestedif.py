email="foo@gmail.com"
password="foo@1234"

useremail=str(input("Enter email: "))
userpasswd=str(input("Enter password: "))

if(useremail==email):
    if(userpasswd==password):
        print("login")
    else:
        print("incorrect password")
else:
    print("user not found")