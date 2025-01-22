
while True:
    print("Welcome My App")
    print("1 to run the app\n2 to stop the app")
    choice=int(input("Enter Your choice"))

    if choice==1:
        name=str(input("Enter your name: "))
        print(name)
    elif choice==2:
        break
    else:
        print("invaild choice")