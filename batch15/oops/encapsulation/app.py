from libs.user import User
while True:
    print("----------INSTAGRAM CLI-------------")
    print("1 to signup")
    print("2 to login")
    print("3 to Exit")
    choice = int(input("Enter your choices: "))
    if choice==1:
        name=str(input("Enter username: "))
        email=str(input("Enter email: "))
        password=str(input("Enter password: "))
        age=int(input("Enter your age: "))
        u1=User(name,email,password,age)
        print("signup success")
    elif choice==2:
        email=str(input("Enter email: "))
        password=str(input("Enter password"))
        if email==u1.getemail():
            if password ==u1.getpassword():
                while True:
                    print(f"Welcome {u1.getname()}")
                    print("1 to view profile")
                    print("2 to update username")
                    print("3 to logout")
                    choice2=int(input("Enter your choice: "))
                    if choice2==1:
                        print("------Profile--------")
                        print(f"Name:{u1.getname()}")
                        print(f"Age: {u1.getage()}")
                    elif choice2==2:
                        newname=str(input("Enter new username: "))
                        u1.setname(newname)
                        print("Name is update")
                    elif choice2==3:
                        print("Logout")
                        break
                    else:
                        print("Invaild choice !!")
            else:
                print("Incorrect password")
        else:
            print("user not found")
    elif choice ==3:
        print("Exiting...")
        break
    else:
        print("Invaild choice !")
