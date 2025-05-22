from model import evennum,oddnum
from model.animation import InstagramBanner
from model.color import Color

banner=InstagramBanner()
banner.display_banner()

while True:
    print(f"{Color.YELLOW}[1]{Color.RESET} {Color.GREEN}To Find Even number{Color.GREEN}")
    print(f"{Color.YELLOW}[2]{Color.RESET} {Color.GREEN}To Find Odd number{Color.GREEN}")
    print(f"{Color.YELLOW}[3]{Color.RESET} {Color.GREEN}To Exiting..{Color.GREEN}")
    print(f"{Color.YELLOW}-----------------------------------{Color.RESET}")
    choice=int(input("Enter your choice: "))

    if choice==1:
        num=int(input("Enter the number: "))
        result=evennum.even(num)
        print(f"Even number in {num} : {result}")
        print(f"{Color.YELLOW}-----------------------------------{Color.RESET}")

    elif choice==2:
        num=int(input("Enter the number: "))
        result=oddnum.odd(num)
        print(f"Odd number in {num} : {result}")
        print(f"{Color.YELLOW}-----------------------------------{Color.RESET}")

    elif choice==3:
        print(f"{Color.RED}Exiting...{Color.RESET}")
        break
    else:
        print("Invaild choice")


