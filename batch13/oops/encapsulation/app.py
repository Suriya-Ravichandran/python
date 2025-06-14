from lib.user import User
while True:
    print("Instagram CLI")
    print("1 to signin")
    print("2 to login")
    print("3 to Exit")
    choice = int(input("Enter your choice: "))

    if choice==1:
        username=str(input("Enter your name: "))
        email=str(input("Enter your Email: "))
        age=int(input("Enter your age: "))
        password=str(input("Enter Your password: "))
        u1=User(username,email,password,age)
        print("Signin Sucess !!")
    elif choice ==2:
        email=str(input("Enter your Email: "))
        password=str(input("Enter Your password: "))
        if u1.getemail()==email:
            if u1.getpassword()==password:
                print("Login success")
                print("----------------")
                while True:
                    print(f"Welcome {u1.getname()}")
                    print("1 to view Profile")
                    print("2 to update profile")
                    print("3 to logout")
                    choice1=int(input("Enter your choice"))
                    if choice1==1:
                        print("----Profile details----")
                        print(f"Name: {u1.getname()}")
                        print(f"Age: {u1.getage()}")
                        print(f"Email: {u1.getemail()}")
                        print(f"Passwor: {u1.getpassword()}")
                    elif choice1==2:
                         name=str(input("Enter name: "))
                         u1.setname(name)
                         print("Profile updated !!")
                    elif choice1==3:
                        print("Logout...")
                        break
                    else:
                        print("Invaild choice !!")
            else:
                print("Incorrect password")
        else:
            print("User not found")
       
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invaild choice")