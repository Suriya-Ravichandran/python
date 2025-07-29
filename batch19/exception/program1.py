
while True:
    
    try:
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        result=num1/num2
        print(f"Result: {result}")
    except Exception as e:
        print(e)
        # print("press q to exit")
        # print("press Any key to continue")
        # choice=str(input("Enter your choice: "))
        # if choice=="q":
        #     print("exit..")
        #     break
        # else:
        #     continue

    else:
        print("No error")
    finally:
        print("Program successs")



    
