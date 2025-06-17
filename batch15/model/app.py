from lib import calculator
while True:
    print("-------Welcome simple calculator --------")
    print("1 to Add")
    print("2 to sub")
    print("3 to mul")
    print("4 to div")
    print("5 to Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        print(f"Result: {calculator.add(num1,num2)}")
    elif choice==2:
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        print(f"Result: {calculator.sub(num1,num2)}")
    elif choice==3:
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        print(f"Result: {calculator.mul(num1,num2)}")
    elif choice==3:
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        print(f"Result: {calculator.div(num1,num2)}")

    else:
        print("Exiting...")
        break
    
