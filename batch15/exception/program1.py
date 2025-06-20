while True:
    
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    try:
        Result=num1/num2
        print(f"Result: {Result}")
    except Exception as e:
        print(e)
    else:
        print("No error")
    finally:
        print("Program run successfully")
