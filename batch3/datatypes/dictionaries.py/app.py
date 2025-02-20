from creadentials import user

Email=str(input("Enter Email: "))
Password=str(input("Enter Password: "))

verifyEmail=user.mydict["Email"]
verifyPassword=user.mydict["Password"]

# print(verifyEmail)
# print(verifyPassword)

def success():
    return 0

if(Email==verifyEmail):
    if(Password==verifyPassword):
        print("Login Success")
        Password=success()
        verifyPassword=success()
        
    else:
        print("Incorrect Password")
else:
    print("Email Not Found")


print(Password)
