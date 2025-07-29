from instalib.user import User

while True:
    print("-----Mini Instagram---------")
    print("1 to Signup")
    print("2 to Signin")
    print("3 to Exit")

    choice =int(input("Enter your choice: "))
    if choice==1:
        name=str(input("Enter your Name: "))
        email=str(input("Enter your Email: "))
        password=str(input("Enter your Password: "))
        bio=str(input("Enter your bio: "))
        age=int(input("Enter your age: "))
        u1=User(name,email,password,bio,age)
        print("Signup Success")

    elif choice==2:
        email=str(input("Enter your Email: "))
        password=str(input("Enter your Password: "))
        if email==u1.getemail():
            if password==u1.getpassword():
                    while True:
                        print(f"Welcome {u1.getname()}")
                        print("1 to edit profile")
                        print("2 to change password")
                        print("3 to logout")
                        choice=int(input("Enter your choice: "))
                        if choice==1:
                            name=str(input("Enter your new name: "))
                            u1.setname(name)
                            print("name change success")
                        elif choice==2:
                            password=str(input("Enter your current password: "))
                            if password==u1.getpassword():
                                newpassword=str(input("Enter new password: "))
                                u1.setpassword(newpassword)
                                print("Password changed")
                            else:
                                print("current password incorrect")
                        elif choice==3:
                            print("Logout")
                            break
                        else:
                            print("invaild choice ")
            else:
                print("Incorrect password")
        else:
            print("User not found")
    elif choice==3:
        print("Exiting...")
        break
    else:
        print("invaild choice")