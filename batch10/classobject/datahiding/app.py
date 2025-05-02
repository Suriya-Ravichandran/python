from model.User import User


# # tesing 

# user1=User("Foo","foo@gmail.com","foo@123")
# user2=User("Boo","boo@gmail.com","boo@123")

# print(user1.getName())
# print(user2.getName())
# print(user1.getName())
while True:
    print("1 to signin , 2 to login")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        print("------Sign page------")
        name=str(input("Enter your name: "))
        email=str(input("Enter your email: "))
        password=str(input("Enter your password: "))
        user1=User(name,email,password)
        print("---------Signin successfully-------- ")
        print("\n")
    elif choice == 2:
        email=str(input("Enter your email: "))
        password=str(input("Enter your password: "))
        verifyuser=user1.getEmail()
        verifypassword=user1.getPassword()
        if email == verifyuser:
            if password==verifypassword:
                while True:

                    print("-------Dashboard--------")
                    print(" 1 to edit password, 2 to view profile, 3 to logout")
                    print(f"Welcome {user1.getName()}")
                    choice=int(input("Enter your choice: "))
                    if choice ==1:
                        password=str(input("Enter your old password: "))
                        if (password == user1.getPassword()):
                            Newpassword=str(input("Enter your New password: "))
                            user1.setPassword(Newpassword)
                            print("Password change success")
                        elif choice==2:
                            print("-------Profile page--------")
                            print("Name:",user1.getName())
                            print("Email:",user1.getEmail())
                            print("Password:",user1.getPassword())
                        elif choice==3:
                            print("Logout...")
                            break

            else:
                print("Incorrect password")
        else:
            print("User not found")
    else:
        print("Invaild choice !!")

