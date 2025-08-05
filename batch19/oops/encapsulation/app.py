from colorama import Fore, Back, Style, init
import random
from insta.user import User

while True: 
    # Initialize colorama
    init(autoreset=True)

    heart_banner = """
      ******       ******  
    *********   ********* 
    *********** *********** 
    *************************
    ************************
      **********************
      ********************
        ****************
          ************
            ********
              ****
                **
    """

    for line in heart_banner.splitlines():
        print(Fore.RED + line)
    print(Fore.YELLOW + "----Welcome To Mini instagram----")

    print(Fore.YELLOW +"--------------------------------------------")
    print(Fore.YELLOW +"1 "+ Fore.BLUE + "Signin")
    print(Fore.YELLOW +"2 "+ Fore.BLUE + "Signup")
    print(Fore.YELLOW +"3 "+ Fore.BLUE + "exit")
    choice=int(input(Fore.RED + "Enter your choice: "))
    if choice==1:
        email=str(input("Enter your email: "))
        password=str(input("Enter your password: "))
        if u1.get_email()==email:
            if u1.get_password()==password:
                while True:
                  print("Welcome",u1.get_name())
                  print("1 to view profile")
                  print("2 to change password")
                  print("3 to logout")
                  choice =int(input("Enter your choice: "))
                  if choice==1:
                      print("------ profile details---------")
                      print(f"Name: {u1.get_name()}")
                      print(f"Email: {u1.get_email()}")
                      print(f"Bio: {u1.get_bio()}")
                  elif choice==2:
                      password=str(input("Enter your password: "))
                      if password==u1.get_password():
                          newpassword=str(input("Enter your new password: "))
                          u1.set_password(newpassword)
                          print("Password changed")
                      else:
                          print("Your current password is not match")
                  elif choice==3:
                      print("Logout")
                      break
            
                    
            else:
                print("password incorrect")
        else:
            print("User not found")
    elif choice==2:
        name=str(input("Enter your name: "))
        email=str(input("Enter your email: "))
        password=str(input("Enter your password: "))
        bio=str(input("Enter your bio: "))
        u1=User(name,email,password,bio)
        print(Fore.GREEN +"Sigup sucess")
    elif choice==3:
        print(Fore.RED+"Exiting")
        break
    else:
        print(Fore.YELLOW + "Invaild choice !!")

