from loginlib.user import User

while True:

    print("1 to signup")
    print("2 to signin")
    print("3 to exit")
    choice=int(input("Enter your choice: "))

    if choice==1:
        name=str(input("Enter your name: "))
        email=str(input("Enter your email: "))
        password=str(input("Enter your password: "))
        bio=str(input("Enter your bio: "))
        u1=User(name,email,password,bio)
        print("Signup success")
    elif choice==2:
        email=str(input("Enter your email: "))
        password=str(input("Enter your password: "))
        if email==u1.get_email():
            if password==u1.get_password():
                while True:
                    print(f"welcome: {u1.get_name()}")
                    print("1 to change password")
                    print("2 to logout")
                    choice1=int(input("Enter your choice: "))
                    if choice1==1:
                        current=str(input("Enter your cuurent password"))
                        if current==u1.get_password():
                            new=str(input("Enter new password: "))
                            u1.set_password(new)
                            print("Password change success")
                        else:
                            print("current password incorrect")
                    elif choice1==2:
                        print("logout")
                        break
                    else:
                        print("Inavild choice")
            else:
                print("Incorrect password")
        else:
            print("User not found")
    elif choice==3:
        print("Exiting")
        break
    else:
        print("invaild choice")