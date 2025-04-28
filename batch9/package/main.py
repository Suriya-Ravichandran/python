from apps import calculator

while True:
    print("Welcome To simple calculator")
    print("Press 1 to add")
    print("Press 2 to sub")
    print("Press 3 to Mul")
    print("Press 4 to div")
    choice=int(input("Enter Your Choice: "))
    if(choice==1):
        value1=int(input("Enter Num 1: "))
        value2=int(input("Enter Num 2: "))
        result=calculator.add(value1,value2)
        print("Result:",result)
        print("---------------------")
