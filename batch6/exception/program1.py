while True:
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    try:
        print("Result: ",num1/num2)
    except:
        print("Cannot divided by zero")
    else:
        print("No error")
    finally:
        print("try block and expect block is excuted")