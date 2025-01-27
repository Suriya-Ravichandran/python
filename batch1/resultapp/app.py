#INSERT INTO `result` (`id`, `name`, `dob`, `tamil`, `computer`, `maths`) VALUES ('1', 'foo', '1-2-2000', '75', '85', '65');

import model.result

while True:
    print("--------Welcome to Exam Result App-----------")
    print("Press 1 to Student Login\nPress 2 to Admin login\nPress 0 to Exit")
    login=int(input("Enter your choice"))
    if(login==1):
        print("--------Student login success------")
        while True:
            print("Press 1 to view result\nPress 2 to Exit ")
            action=int(input("Enter your choice"))
            if(action==1):
                id=int(input("Enter your ID: "))
                # dob=str(input("Enter your DOB: "))
                model.result.getresult(id)
            elif(action==2):
                print("Exiting Student.....")
                break
            else:
                print("Invaild choice")
    elif(login==0):
        print("Exiting...")
        break
    else:
        print("invaild choice")





