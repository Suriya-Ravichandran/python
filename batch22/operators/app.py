password=str(input("Enter your password: "))
confirmpassword=str(input("Enter confirm password: "))

if password and confirmpassword:
    if password==confirmpassword:
        print("Password match")
    else:
        print("Password not match")
else:
    print("Password field is required")