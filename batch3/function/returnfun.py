def signin(email,password="1234"):
    if(password=="1234"):
        demail=email
        dpassword=password
        return 1
    else:
        return 0


email=str(input("Enter your Email: "))
# password=str(input("Enter your password: "))

verify=signin(email)
print(verify)

if(verify==1):
    print("login success")
else:
    print("login failed")

