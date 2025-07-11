while True:
    print("------Traffic Signal-------")
    print("1 to Red")
    print("2 to Yellow")
    print("3 to Green")
    print("4 to Exit")
    choice =int(input("Enter your choice: "))

    if choice==1:
        print("Red")
    elif choice==2:
        print("Yellow")
    elif choice==3:
        print("Green")
    elif choice==4:
        print("Exiting ....")
        break
    else:
        print("Invaild choice")