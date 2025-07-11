from calcu import calculib

while True:
    print("------Calculator App--------")
    print("1 to Add")
    print("2 to Sub")
    print("3 to Mul")
    print("4 to Div")
    print("5 to Mod")
    print("0 to Exit")
    choice = int(input("Enter your choice: "))

    if choice==1:
        num1=int(input("Enter Num1: "))
        num2=int(input("Enter Num2: "))
        print("Result:",calculib.add(num1,num2))
    elif choice==2:
        num1=int(input("Enter Num1: "))
        num2=int(input("Enter Num2: "))
        print("Result:",calculib.sub(num1,num2))
    elif choice==3:
        num1=int(input("Enter Num1: "))
        num2=int(input("Enter Num2: "))
        print("Result:",calculib.mul(num1,num2))
    elif choice==4:
        num1=int(input("Enter Num1: "))
        num2=int(input("Enter Num2: "))
        print("Result:",calculib.div(num1,num2))
    elif choice==5:
        num1=int(input("Enter Num1: "))
        num2=int(input("Enter Num2: "))
        print("Result:",calculib.mod(num1,num2))
    elif choice==0:
        print("Exiting....")
        break
    else:
        print("Invaild choice")
