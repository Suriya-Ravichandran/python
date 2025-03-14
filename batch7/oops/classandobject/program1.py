from module.user import User

while True:
    print("1 to signup\n2 to login")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Username: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        u1 = User(name, email, password)
        print("Signup successful!")

    elif choice == 2:
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        u1.login(email, password)
