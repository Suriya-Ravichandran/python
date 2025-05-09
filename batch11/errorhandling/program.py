while True:
    try:
        num1=int(input("Enter Num1: "))
        num2=int(input("Enter Num2: "))
        print("Result:",num1/num2)
    except Exception as e:
        print(f"Error: {e}")
    
    else:
        print("No error")
    
    finally:
        print("Try except is run successfully")

