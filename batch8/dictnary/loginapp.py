import data

email=str(input("Enter your Email: "))
password=str(input("Enter your Password: "))

if email==data.data["email"]:
    if password==data.data["password"]:
        print(f"Welcome {data.data["name"]} !!!!")
    else:
        print("Incorrect Password")
else:
    print("User Not Found !!!")