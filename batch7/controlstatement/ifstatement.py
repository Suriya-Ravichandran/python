print("Press 1 to Red\nPress 2 to Yellow\nPress 3 to green\nPress 0 to exit")

while True:
    choice=int(input("Enter your choice: "))

    if choice == 1:
        print("\033[31mRed\033[0m")     # Red
    elif choice == 2:
        print("\033[33mYellow\033[0m")  # Yellow
    elif choice == 3:
        print("\033[32mGreen\033[0m")   # Green
    elif choice == 0:
        print("Exiting....")
        break
    else:
        print("invaid choice !!")