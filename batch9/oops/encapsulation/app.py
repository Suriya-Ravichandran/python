from model.User import User

while True:
    print("1 to signup,2 to login")
    choice = int(input("Enter your choice: "))
    if choice==1:
        username=str(input("Enter username: "))
        age=int(input("Enter age: "))
        email=str(input("Enter email: "))
        password=str(input("Enter password: "))
        u1=User(username,age,email,password)
    elif choice == 2:
        email=str(input("Enter email: "))
        password=str(input("Enter password: "))
        verifypassword=u1.getPassword()
        if(email==u1.getEmail()):
            if(password==verifypassword):
                print(f"Welcome {u1.getName()}")
                print(f"-----Profile-------")
                print(f"Name: {u1.getName()}")
                print(f"Age: {u1.getAge()}")
                print(f"Email: {u1.getEmail()}")
                print(f"password: {u1.getPassword()}")
                while True:
                    print("1 to change password,2 to logout")
                    choice=int(input("Enter your choice: "))
                    if choice==1:
                        Oldpassword=str(input("Enter your Old Password: "))
                        if Oldpassword==u1.getPassword():
                            password=str(input("Enter New password: "))
                            u1.setPassword(password)
                            print("Password change successfully")
                    elif choice==2:
                        print("Logout")
                        break
            else:
                print("Incorrect password")
        else:
            print("User Not found")
