while True:
    print("Press 1 To Red\nPress 2 to Yellow\nPress 3 to Green\nPress 0 to Exit")
    choice=int(input("Enter Your Choice: "))

    if choice==1:
        print("Red")
    elif choice==2:
        print("Yellow")
    elif choice==3:
        print("Green")
    elif choice==0:
        print("Exiting...")
        break
    else:
        print("Invaild Choice !!")
