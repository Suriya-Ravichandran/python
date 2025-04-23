a=int(input("Enter num 1: "))
b=int(input("Enter num 2: "))
try:
    result=a/b
    print("Result: ",result)
except:
    print("division by zero")
else:
    print("No error")

finally:
    print("code run sucessfully")
