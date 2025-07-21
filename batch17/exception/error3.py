while True:
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    try:
        result=num1/num2
        print(f"Result: {result}")
    except Exception as e:
        print(e)

    else:
        print("No error")
    finally:
        print("Code run successfully")


