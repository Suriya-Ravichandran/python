from user import settergetter

print("Welcome To Simple Bio App")
while True:
    print("1 to Login\n2 to Signup\n0 to Exit")
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        Email=str(input("Enter Your Email: "))
        Password=str(input("Enter Your Password: "))
        verifyEmail=settergetter.getemail()
        verifyPassword=settergetter.getpassword()
        if (Email==verifyEmail):
            if(Password==verifyPassword):
                print(f"login success {settergetter.getname()}")
                while True:
                    print("1 to view profile\n2 to Edit Profile\n0 to Logout")
                    choice1=int(input("Enter Your choice: "))
                    if choice1==1:
                        print("Your Profile")
                        print(f"Name: {settergetter.getname()}")
                        print(f"Age: {settergetter.getage()}")
                        print(f"Email: {settergetter.getemail()}")
                        print(f"Password: {settergetter.getpassword()}")
                    elif choice1==2:
                        Email=str(input("Enter Email: "))
                        Password=str(input("Enter Password: "))
                        name=str(input("Enter Name: "))
                        age=str(input("Enter Your Age: "))
                        settergetter.setname(name)
                        settergetter.setage(age)
                        settergetter.setemail(Email)
                        settergetter.setpassword(Password)
                        print("Edit profile Success")
                    else:
                        print("Logout....")
                        break

            else:
                print("Incorrect Password !!")
        else:
            print("Email Not found")
    elif choice==2:
        Email=str(input("Enter Email: "))
        Password=str(input("Enter Password: "))
        name=str(input("Enter Name: "))
        age=str(input("Enter Your Age: "))
        settergetter.setname(name)
        settergetter.setage(age)
        settergetter.setemail(Email)
        settergetter.setpassword(Password)
        print("signup success...")
    elif choice==0:
        print("Exiting....")
        break
    else:
        print("Invaild choice...")
    