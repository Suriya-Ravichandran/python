useremail=str(input("Enter your Email: "))
password=str(input("Enter your password: "))

email="foo@gmail.com"
passwd="1234"


if useremail==email:
    if password==passwd:
        print("Login success")
    else:
        print("Incorrect password")
else:
    print("User not found")
