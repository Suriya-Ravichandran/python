def add(value1,value2):
    return value1+value2

def sub(value1,value2):
    return value1-value2

def mul(value1,value2):
    return value1*value2

def div(value1,value2):
    return value1/value2

print("Press 1 to add\nPress 2 to sub\nPress 3 to Mul\nPress 4 to Div\nPress 0 to exit")

while True:
    choice=int(input("Enter the choice: "))
    if choice==1:
        value1=int(input("Enter Value 1: "))
        value2=int(input("Enter Value 2: "))
        print("Result:",add(value1,value2))

    elif choice==2:
        value1=int(input("Enter Value 1: "))
        value2=int(input("Enter Value 2: "))
        print("Result:",sub(value1,value2))

    elif choice==3:
        value1=int(input("Enter Value 1: "))
        value2=int(input("Enter Value 2: "))
        print("Result:",mul(value1,value2))
    elif choice==4:
        value1=int(input("Enter Value 1: "))
        value2=int(input("Enter Value 2: "))
        print("Result:",div(value1,value2))
    elif choice==0:
        print("Exit....")
        break

    else:
        print("invaild choice")