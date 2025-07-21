try:
    filename=str(input("Enter filename: "))
    f=open(filename,"x")
    print("File created success")
except Exception as e:
    print(e)
    while True:
        print("1 to rename")
        print("2 to cancel")
        choice=int(input("Enter your choice: "))

        if choice==1:
            filename=str(input("Enter filename: "))
            f=open(filename,"x")
            print("File created success")
            break
        elif choice==2:
            print("file creation failed")
            break
        else:
            print("Invaild choice")