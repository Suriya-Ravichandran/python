file_name=str(input("Enter the filename: "))
try:
    f=open(file_name,"x")
    print("file create successfully")
except FileExistsError:
    flag=0
    
    while True:
        if flag==0:
            print("File already Exits")
            print("press 1 to rename,Press 2 to cancle")
            
            choice=int(input("Enter your choice: "))
            
            if choice == 1:
                while True:
                    rename=str(input("Rename your file:"))
                    try:
                        f=open(rename,"x")
                        print("file create successfully")
                        flag=1
                        break
                    except FileExistsError:
                        print("File already Exits")
                        break
                    
            elif choice == 2:
                print("File creation cancle !!")
                break
            else:
                print("invaild choice !")
        elif flag==1:
            break
        else:
            print("File creation failed")
