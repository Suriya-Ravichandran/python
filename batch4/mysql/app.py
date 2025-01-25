import controller
import controller.user

print("-----welcome app---------")
print("Press 1 to user\nPress 2 to Admin")
login=int(input("Enter your choice: "))

if login==1:
    print("-------login sucess------")
    while True:
        print("Press 1 to view profile\nPress 2 to update profile\nPress 3 to edit profile\nPress 4 to delete profile\nPress 0 to exit")
        action=int(input("Enter choice: "))
        if action==1:
            print("--------user profile--------")
            controller.user.getuserdata()                                                                                                                                                                                                                                                                                                                                                             
        elif action==2:
            name=str(input("Enter Name: "))
            email=str(input("Enter Email: "))
            dept=str(input("Enter Dept: "))
            response=controller.user.setuserdata(name,email,dept)
            print(response)
        
        elif action==3:
            name=str(input("Enter Name: "))
            email=str(input("Enter Email: "))
            dept=str(input("Enter Dept: "))
            response=controller.user.edituserdata(name,dept,email)
            print(response)
        
        elif action==4:
            email=str(input("Enter Email: "))
            response=controller.user.deleteuserdata(email)
            print(response)
        elif action==0:
            print("Exiting.....")
            break
            
else:
    print("invaild")