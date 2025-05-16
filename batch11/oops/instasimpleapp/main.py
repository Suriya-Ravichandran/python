from module.user import User
from module.animation import InstagramBanner
from module.color import Color

banner=InstagramBanner()
banner.display_banner()

while True:
    print(f"{Color.YELLOW}[1] - {Color.RESET}{Color.BLUE}login {Color.RESET}\n{Color.YELLOW}[2] -{Color.RESET}{Color.BLUE} signin{Color.RESET}\n{Color.YELLOW}[3] -{Color.RESET}{Color.BLUE} Exit{Color.RESET}")
    choice=int(input(f"{Color.GREEN}Enter your choice: {Color.RESET}"))
    if (choice == 1):
        email=str(input("Enter your Email: "))
        password=str(input("Enter your password: "))
        if(email==u1.getemail()):
            if(password==u1.getpassword()):
                print(f"Welcome{Color.GREEN} {u1.getname()}{Color.RESET}")
            else:
                print(f"{Color.RED} Incorrect password {Color.RESET}")
        else:
           print(f"{Color.RED} User not found ! {Color.RESET}")
        
    elif (choice==2):
        name=str(input("Enter your name: "))
        email=str(input("Enter your Email: "))
        password=str(input("Enter your password: "))
        age=int(input("Enter your age: "))
        u1=User(name=name,email=email,password=password,age=age)
        print("Signup Successfull !!")
    elif (choice==3):
            print("Good Bye !!")
            break
    else:
        print("Invaild choice !!")
