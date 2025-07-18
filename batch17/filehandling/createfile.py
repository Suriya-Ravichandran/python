try:
    filename=str(input("Enter filename: "))
    f=open(filename,"x")
    print("File created success")
except Exception as e:
    print(e)
    while True:
        choice=int(input("Rename to press 1 or cancel press 2: "))
        if choice==1:
            filename=str(input("Enter filename: "))
            f=open(filename,"x")
            print("File created success")
            break
        elif choice==2:
            print("file creation failded")
            break
        else:
            print("invalid choice")
