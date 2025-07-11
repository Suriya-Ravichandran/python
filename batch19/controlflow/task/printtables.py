while True:

    print("-----------Tables Genrator------------")
    print("1 to get Entire table")
    print("2 to get a single tables value: ")
    print("0 to Exit")
    choice =int(input("Enter your choice: "))

    if choice==1:
        tables=int(input("Enter Which Table You Want: "))
        times=int(input("Enter How many Times You Want: "))
        print("-------Tables----------")
        for x in range(1,times+1):
            print(f"{tables} x {x} = {tables*x}")

    elif choice==2:
        tables=int(input("Enter Which Table You Want: "))
        times=int(input("Enter How many Times You Want: "))
        print("-------Tables----------")
        result=0
        for x in range(1,times+1):
            result=tables*x
        print(f"{tables} x {x} = {result}")

    elif choice==0:
        print("Exiting....")
        break
    else:
        print("Invalid choice !!!")


