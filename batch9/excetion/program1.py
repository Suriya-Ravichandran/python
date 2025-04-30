while True:
    a=int(input("Enter the num1: "))
    b=int(input("Enter the num2: "))
    try:
        result=a/b
        print(result)
    except:
        print("divide zero error")
    else:
        print("No error")
    finally:
        print("Code Runing succefully")
    