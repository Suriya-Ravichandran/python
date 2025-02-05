def signin(email,password):
    if(email=="suriya@gmail.com" and password=="1234"):
        # demail=email
        # dpassword=password
        return 1
    else:
        return 0


email=str(input("Enter your Email: "))
password=str(input("Enter your password: "))

verify=signin(email,password)
print(verify)

if(verify==1):
    print("login success")
else:
    print("login failed")

