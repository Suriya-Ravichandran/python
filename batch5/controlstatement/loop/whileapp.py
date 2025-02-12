while(True):
    print("1 to Register\n2 to Exit")
    choice=int(input("Enter Your choice"))
    if(choice==1):
        Name=str(input("Enter Sname: "))
        RollNo=int(input("Enter Srollno: "))
        Gender=str(input("Enter Gender: "))
        BloodGroup=str(input("Enter Blood Group: "))
        DataOFBirth=str(input("Enter Date Of Birth: "))
        print("-----Student DataBase------")
        print("---------------------------")
        print("Name:",Name)
        print("RollNo:",RollNo)
        print("Gender:",Gender)
        print("BloodGroup:",BloodGroup)
        print("DataOFBirth:",DataOFBirth)
        print("--------------------------")
    elif(choice==2):
        print("Exiting")
        break
    else:
        print("Invaild choice")