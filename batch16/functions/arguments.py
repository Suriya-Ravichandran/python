def add(value1,value2):
    return value1+value2

def sub(value1,value2):
    print(value1-value2)

def mul(value1,value2):
    print(value1*value2)

def div(value1,value2):
    print(value1/value2)


while True:
    print("Simple calculator")
    print("1 to add")
    print("2 to sub")
    print("3 to mul")
    print("4 to div")
    print("5 to exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        print(f"Result: {add(num1,num2)}")
    elif choice==2:
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        sub(num1,num2)
    elif choice==3:
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        mul(num1,num2)
    elif choice==4:
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        div(num1,num2)
    elif choice==5:
        print("Exiting...")
        break



