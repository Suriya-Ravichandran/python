from mathtool import calcu,square

while True: 
    print("-------Simple Calculator------")
    print("1 to add")
    print("2 to sub")
    print("3 to mul")
    print("4 to div")
    print("5 to find square")
    print("6 to exit")
    print("-------------------------------")
    choice=int(input("Enter your choice: "))

    if choice==1:
        result=calcu.add()
        print(f"Result: {result}")
    elif choice==2:
        result=calcu.sub()
        print(f"Result: {result}")
    elif choice==3:
        result=calcu.mul()
        print(f"Result: {result}")
    elif choice==4:
        result=calcu.div()
        print(f"Result: {result}")
    elif choice==5:
        result=square.getsquarenum()
        print(f"Result: {result}")
    elif choice==6:
        print("Exiting....")
        break
    else:
        print("Invaild choice !")

