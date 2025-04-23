
while True:
    print("PRESS 1 TO RED,PRESS TO 2 YELLOW,PRESS 3 TO GREEN,PRESS 0 TO EXIT..")
    choice=int(input("Enter your choice:"))

    if choice==1:
        print("Red")
    elif choice==2:
        print("Yellow")
    elif choice==3:
        print("Green")
    elif choice==0:
        print("Exiting....")
        break
    else:
        print("invaild choice !!")

