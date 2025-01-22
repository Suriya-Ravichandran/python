user={
    "name":"suriya",
    "email":"suriya@gmail.com",
    "password":"suriyapasswd"
}

email=str(input("Enter Email: "))
password=str(input("Enter password: "))


if user["password"]==password:
    print("welcome ",email)
elif user["password"]!=password:
    print("Incorrect password")
else:
    print("try again later")