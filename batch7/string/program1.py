saltkey="dgfghdgasdahsdushdsyfrwwwrdfj"

def signin(password):
    return saltkey+password+saltkey

def login(verifypassword,password):
    saltedpassword=saltkey+password+saltkey
    if saltedpassword==verifypassword:
        print("Login success")
        return 1
    else:
        print("login failed")
        return 0

password=str(input("Enter your password"))

verifypassword=signin(password)
print("hashpassword:",verifypassword)
password=login(verifypassword,password)

print(password)


