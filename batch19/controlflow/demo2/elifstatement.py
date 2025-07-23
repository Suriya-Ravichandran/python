while True:

    print("1 to red")
    print("2 to green")
    print("3 to yellow")

    choice =int(input("Enter your choice: "))

    if choice==1:
        print("red")
    elif choice==2:
        print("green")
    elif choice==3:
        print("yellow")
    elif choice==4:
        print("Exiting..")
        break
    else:
        print("Invaild choice")