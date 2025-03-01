import subprocess

print("---------Welcome To Simple CLI NOTE Pad------------")



while True:
    print("1 to createFile\n2 to editFile\n3 to ReadFile\n4 to DeleteFile\n0 to Exit")
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        filename=str(input("Enter Filename: "))
        action=["touch",filename]
        subprocess.call(action)
        print("File created Successfully!!")
    elif choice==2:
        filename=str(input("Enter Filename: "))
        action=["nano",filename]
        subprocess.call(action)
        print("File edited Sucessfully!!")

    elif choice==3:
        filename=str(input("Enter Filename: "))
        action=["cat",filename]
        subprocess.call(action)

    elif choice==4:
        filename=str(input("Enter Filename: "))
        action=["rm","-rf",filename]
        subprocess.call(action)
        print("File remove successfully!!")
    elif choice==0:
        print("Exiting....")
        break
    else:
        print("invaild choice !!")
    

