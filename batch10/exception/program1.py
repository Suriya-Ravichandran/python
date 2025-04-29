while True:
    num1=int(input("Enter the num1: "))
    num2=int(input("Enter the num2: "))
    try:
        print(num1/num2)
    except (ZeroDivisionError,FileExistsError) as e:
        print(e)
    else:
        print("no error")
    finally:
        print("Program run successfully")

