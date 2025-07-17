def Etables(tables,times):
    for x in range(1,times+1):
        print(f"{tables} x {x} = {tables*x}")

def Stables(tables,times):
    for x in range(1,times+1):
        result=tables*x
    print(f"{tables} x {x} = {result}")

def Evennumber(num):
    for x in range(num):
        if x%2==0:
            print(x)
    
def oddnumber(num):
    for x in range(num):
        if x%2!=0:
            print(x)


# main app
while True:
    print("1 to Get Entire Tables: ")
    print("2 to Get single Tables: ")
    print("3 to Get Even number: ")
    print("4 to Get ODD number: ")
    print("5 to Exiting")

    choice=int(input("Enter your choice:"))
    if choice==1:
        tables=int(input("Enter your table: "))
        times=int(input("Enter your times: "))
        Etables(tables,times)
    elif choice==2:
        tables=int(input("Enter your table: "))
        times=int(input("Enter your times: "))
        Stables(tables,times)
    elif choice==3:
        num=int(input("Enter your number:"))
        Evennumber(num)
    elif choice==4:
        num=int(input("Enter your number:"))
        oddnumber(num)
    elif choice==5:
        print("Exiting")
        break
    else:
        print("invaild choice")