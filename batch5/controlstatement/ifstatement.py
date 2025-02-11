while(True):
    print("1 to RED\n2 to Yellow\n3 to Green\n0 to exit")
    choice=int(input("Enter your choice: "))

    if choice==1:
        print("RED")
    elif choice==2:
        print("Yellow")
    elif choice==3:
        print("Green")
    elif choice==0:
        print("Exiting...")
        break
    else:
        print("Invaild choice")