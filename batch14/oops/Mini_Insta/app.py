from lib.user import User

while True: 
    print("------MINI INSTA-------")
    print("\n")
    print("1 to signin")
    print("2 to Login")
    print("3 to Exiting")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=str(input("Enter your name: "))
        email=str(input("Enter your email: "))
        password=str(input("Enter your password: "))
        u1=User(name,email,password)
        print("------Signup success--------")
    elif choice==2:
        useremail=str(input("Enter your email: "))
        userpassword=str(input("Enter your password: "))
        if useremail==u1.getemail():
            if(userpassword==u1.getpassword()):
                while True:
                    print(f"Welcome {u1.getname()}")
                    print("1 to Edit username")
                    print("2 to logout")
                    choice2=int(input("Enter your choice: "))
                    if choice2==1:
                        newname=str(input("Enter your name: "))
                        u1.setname(newname)
                        print("name update success")
                    elif choice==2:
                        print("Logout")
                        break
                    else:
                        print("Invaild choice")
            else:
                print("Incorrect password")
        else:
            print("user not found")
    elif(choice==3):
        print("Exiting..")
        break
    else:
        print("invaild choice")