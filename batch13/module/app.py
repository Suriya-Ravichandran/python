from lib import calculator
while True:
    value1=int(input("Enter value1: "))
    value2=int(input("Enter value2: "))

    result=calculator.div(value1,value2)
    print(result)