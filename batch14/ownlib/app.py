from calculator import arithimatic
while True:
    print("Simple calculator app")
    print("1 to Add")
    print("2 to Sub")
    print("3 to Mul")
    print("4 to Div")
    print("5 to Exit")
    print("-------------------------")
    choice = int(input("Enter your choice: "))
    if(choice==1):
        value1=int(input("Enter value 1: "))
        value2=int(input("Enter value 2: "))
        result=arithimatic.add(value1,value2)
        print(f"Result: {result}")
    elif(choice==2):
        value1=int(input("Enter value 1: "))
        value2=int(input("Enter value 2: "))
        result=arithimatic.sub(value1,value2)
        print(f"Result: {result}")
    elif(choice==3):
        value1=int(input("Enter value 1: "))
        value2=int(input("Enter value 2: "))
        result=arithimatic.mul(value1,value2)
        print(f"Result: {result}")
    elif(choice==4):
        value1=int(input("Enter value 1: "))
        value2=int(input("Enter value 2: "))
        result=arithimatic.div(value1,value2)
        print(f"Result: {result}")
    elif(choice ==5):
        print("Exiting..")
        break
    else:
        print("Invaild choice !!!")