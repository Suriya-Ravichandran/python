while True:
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    try:
        result=num1/num2
        print("Result: ",result)
    except ZeroDivisionError as e:
        print(e)
    else:
        print("No error")
    
    finally:
        print("Program run successfully")

    