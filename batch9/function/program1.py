def add(val1,val2):
    return val1+val2

def sub(val1,val2):
    return val1-val2

 
print("Press 1 to ADD,Press 2 to Sub")
choice=int(input("Enter your choice"))
if choice==1:
    num1=int(input("Enter value1: "))
    num2=int(input("Enter value2: "))
    result=add(num1,num2)
    print("Result:",result)




