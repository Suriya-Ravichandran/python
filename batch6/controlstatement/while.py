# i=0

# while i<10:
#     print(i)
#     i+=1

while True:
    print("1 to Add Student\n2 to logout")
    choice=int(input("Enter your choice: "))
    if choice==1:
        Name=str(input("Enter Student Name: "))
        DateofBirth=str(input("Enter Studend Date of Birth: "))
        Age=int(input("Enter Studend age: "))
        Rollno=int(input("Enter Student Roll no: "))
        Mark10=float(input("Enter 10 Mark: "))
        Mark11=float(input("Enter 11 Mark: "))
        Mark12=float(input("Enter 12 Mark: "))
        Percentage10=Mark10/5
        Percentage11=Mark11/6
        Percentage12=Mark12/6
                # student data display here
        print("--------Student Bio Data----------")
        print("Name:",Name)
        print("age: ",Age)
        print(f"Data Of Birth: {DateofBirth}")
        print("RollNo: ",Rollno)
        print(" ")
        print("-----------Your Marks---------------")
        print(f"10th Mark:{Mark10} Percentage: {Percentage10}")
        print(f"11th Mark:{Mark11} Percentage: {Percentage11}")
        print(f"12th Mark:{Mark12} Percentage: {Percentage12}")
    elif choice==2:
        break
    else:
        print("invaid choice")
