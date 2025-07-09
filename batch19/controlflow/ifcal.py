print("----------Calculator App--------------")
print("1 to Add")
print("2 to Sub")
print("3 to mul")
print("4 to div")
print("---------------------------------------")
choice =int(input("Enter your choice: "))
if choice==1:
    print("-------Add-----------")
    num1=int(input("Enter Num 1: "))
    num2=int(input("Enter Num 2: "))
    print(f"Result: {num1+num2}")
elif choice==2:
    print("-------Sub-----------")
    num1=int(input("Enter Num 1: "))
    num2=int(input("Enter Num 2: "))
    print(f"Result: {num1-num2}")
elif choice==3:
    print("-------Mul-----------")
    num1=int(input("Enter Num 1: "))
    num2=int(input("Enter Num 2: "))
    print(f"Result: {num1*num2}")
elif choice==4:
    print("-------Div-----------")
    num1=int(input("Enter Num 1: "))
    num2=int(input("Enter Num 2: "))
    print(f"Result: {num1/num2}")
else:
    print("Invalid choice")
