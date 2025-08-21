def hashgen(password):
    password=password[0:3]
    password=password.capitalize()
    password=password+"$"
    saltkey="fdafdsahfgvytsd"
    saltkey=saltkey.replace("f","&")
    saltkey=saltkey.replace("d","%")
    salted_password=saltkey+password+saltkey
    return salted_password

password=str(input("Enter your password: "))
verifypassword=hashgen(password)
vaildpassword=hashgen(password)

print(verifypassword)
print(vaildpassword)

if verifypassword==vaildpassword:
    print("Login sucess")