from module.user import User
while True:
    print("1 to signin\n2 to login\n3 to Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=str(input("Enter your Name: "))
        email=str(input("Enter your Email: "))
        password=str(input("Enter your Password: "))
        u1=User(name,email,password)
        print("signup sucess")
    elif choice==2:
            email=str(input("Enter your Email: "))
            password=str(input("Enter your Password: "))
            verifyemail=u1.getemail()
            verifypass=u1.getpassword()
            if(email==verifyemail):
                if(password==verifypass):
                    print("login success")
                    while True:
                        print("1 to view Profile\n2 to Editprofile\n3 to Exit")
                        action=int(input("Enter your choice: "))
                        if(action==1):
                            print("Name:",u1.getname())
                            print("Email:",u1.getemail())
                            print("Password:",u1.getpassword())
                        elif(action==2):
                            name=str(input("Enter your Name: "))
                            email=str(input("Enter your Email: "))
                            password=str(input("Enter your Password: "))
                            u1.setname(name)
                            u1.setemail(email)
                            u1.setpassword(password)
                        elif(action==3):
                            break
                        else:
                            print("Invaild choice")
                else:
                    print("Password Incorrect")
            else:
                print("Username not found")
    elif(choice==3):
        break

    else:
        print("invaild choice")