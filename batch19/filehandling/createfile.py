try:
    filename=str(input("Enter file name: "))
    f=open(filename,"x")
    print("file created success")
except Exception as e:
    print(e)
    while True:
        choice=int(input("Enter 1 to rename or 0 cannel: "))
        if choice==1:
            filename=str(input("Enter file name: "))
            f=open(filename,"x")
            print("file created success")
            break
        elif choice==0:
            print("File creation cannel")
            break
        else:
            print("invaild choice !")
        
