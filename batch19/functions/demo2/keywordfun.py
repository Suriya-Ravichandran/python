def userdata(name,email,password,):
    print("-----------User data---------")
    print("Name->",name)
    print("Email->",email)
    print("Password->",password)


name=str(input("Enter your name: "))
email=str(input("Enter your Email: "))
password=str(input("Enter your password: "))

userdata(email=email,name=name,password=password)