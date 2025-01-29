def add(val1,val2):
    print(f"Result: {val1+val2}")

def sub(val1,val2):
    print(f"Result: {val1-val2}")

def mul(val1,val2):
   print(f"Result: {val1*val2}")

def div(val1,val2):
    print(f"Result: {val1/val2}")



print("-------WELCOME TO CALCULATOR---------")
while True:
    print("press 1 to add,2 to sub,3 to mul, 4 to div,0 to exit")
    print("-------------------------------------------------------")
    operation=int(input("Enter your choice: "))
    if(operation==1):
        val1=int(input("Enter first value: "))
        val2=int(input("Enter second value: "))
        add(val1,val2)
    elif(operation==2):
        val1=int(input("Enter first value: "))
        val2=int(input("Enter second value: "))
        sub(val1,val2)
    elif(operation==3):
        val1=int(input("Enter first value: "))
        val2=int(input("Enter second value: "))
        mul(val1,val2)
    elif(operation==4):
        val1=int(input("Enter first value: "))
        val2=int(input("Enter second value: "))
        div(val1,val2)
    elif(operation==0):
        print("Exit....")
        break
    else:
        print("Invaild choice")

