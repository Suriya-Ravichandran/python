while True:
    try:
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        result=num1/num2
        print(f"Result: {result}")
    except KeyboardInterrupt:
        choice=str(input("Enter q to exit or type any to continue:"))
        if choice=="q":
            print("Exiting")
            break
        else:
            continue
    except Exception as e:
        print(e)
    else:
        print("No error")

    finally:
        print("Code run successfully")