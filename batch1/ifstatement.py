while(True):
    print("Press 1 to Age checker")
    print("Press 2 to register for Voter")
    print("Press 0 to Exit")

    # get input from user
    choice=int(input("Enter Your Choice: "))
    if(choice==1): #age checker
        while(True):
            print("Welcome To Age Checker")
            print("Press 0 to Exit")
            print("Press 1 to continue")
            choice=int(input("Enter your choice:"))
            if(choice==1):
                Name=str(input("Enter Name: "))
                age=int(input("Enter age: "))
                
                # checking age here
                if(age>=18):
                    print(f"Your Age is {age} your Eligable to Vote")
                    print(f"Welcome you new voter {Name}")
            elif(choice==0):
                break

    elif(choice==2): #registration form
        Name=str(input("Enter Name: "))
        age=int(input("Enter age: "))
        Aadhar=int(input("Enter Aadhar Id: "))
        print("Your Registration Successfull")
        print("This is your Details:")
        print(f"Name:{Name}")
        print(f"Age: {age}")
        print(f"Aadhar: {Aadhar}")
    else:
        exit()


