from colorama import Fore, Back, Style, init
import random
from insta.user import User
init(autoreset=True)  # Automatically resets color after each print


from colorama import Fore, Back, Style, init

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
while True: 
    print(Fore.YELLOW +"--------------------------------------------")
    print(Fore.YELLOW +"1 "+ Fore.BLUE + "Signin")
    print(Fore.YELLOW +"2 "+ Fore.BLUE + "Signup")
    print(Fore.YELLOW +"3 "+ Fore.BLUE + "exit")
    choice=int(input(Fore.RED + "Enter your choice: "))
    if choice==1:
        pass
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

