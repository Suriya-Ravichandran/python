#INSERT INTO `result` (`id`, `name`, `dob`, `tamil`, `computer`, `maths`) VALUES ('1', 'foo', '1-2-2000', '75', '85', '65');

import model.result

while True:
    print("--------Welcome to Exam Result App-----------")
    print("Press 1 to Student Login\nPress 2 to Admin login\nPress 0 to Exit")
    login=int(input("Enter your choice: "))
    if(login==1):
        print("--------Student login success------")
        while True:
            print("Press 1 to view result\nPress 2 to Exit ")
            action=int(input("Enter your choice: "))
            if(action==1):
                id=int(input("Enter your ID: "))
                # dob=str(input("Enter your DOB: "))
                model.result.getresult(id)
            elif(action==2):
                print("Exiting Student.....")
                break
            else:
                print("Invaild choice")
    elif(login==2):
        while True:
            print("---------Admin Login Sucess-------")
            print("Press 1 to View result\nPress 2 to Add result\nPress 3 to Upadate\nPress 4 to Delete\nPress 0 To Exit")
            action=int(input("Enter your choice: "))
            if(action==1):
                model.result.getallresult()
            elif(action==2):
                id=int(input("Enter SID: "))
                name=str(input("Enter name: "))
                dob=str(input("Enter Dob: "))
                tamil=int(input("Enter Tamil Mark: "))
                computer=int(input("Enter computer Mark: "))
                maths=int(input("Enter maths Mark: "))
                model.result.addresult(id,name,dob,tamil,computer,maths)
            elif(action==3):
                id=int(input("Enter SID: "))
                name=str(input("Enter name: "))
                dob=str(input("Enter Dob: "))
                tamil=int(input("Enter Tamil Mark: "))
                computer=int(input("Enter computer Mark: "))
                maths=int(input("Enter maths Mark: "))
                model.result.updateresult(name,dob,tamil,computer,maths,id)
            

            elif(action==4):
                id=int(input("Enter SID: "))
                model.result.Deleteresult(id)

            elif(action==0):
                print("Admin Exiting....")
                break
            else:
                print("invaild choice")
    elif(login==0):
        print("Exiting...")
        break
    else:
        print("invaild choice")





