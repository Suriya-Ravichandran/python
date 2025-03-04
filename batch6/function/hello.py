def verifypassword(password):
    verifypassword="suriya123"
    if verifypassword==password:
        return 1
    else:
        return 0


password=str(input("Enter password: "))
password=verifypassword(password)
check=password

if check==1:
    print("login success")
else:
    print("Login Failed")

print(password)

