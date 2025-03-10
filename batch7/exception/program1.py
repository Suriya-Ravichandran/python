def add(value1,value2):
    return value1+value2

def sub(value1,value2):
    return value1-value2

def mul(value1,value2):
    return value1*value2

def div(value1,value2):
    try:
        result=value1/value2
        return result
    except:
        return "INIFINTY"
    else:
        print("Block is Not exected")
    finally:
        print("Try block is executed")
while True:
    print("To exit press 0\n1 To Go Calculator")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        while True:
              print("1 to add\n2 to sub\n3 to mul\n4 to div\n0 to Exit")
              action=int(input("Enter your Choice: "))
              if(action==1):
                  result=add(num1,num2)
                  print("Result:",result)
              elif(action==2):
                  result=sub(num1,num2)
                  print("Result:",result)
              elif(action==3):
                  result=mul(num1,num2)
                  print("Result:",result)
              elif(action==4):
                  result=div(num1,num2)
                  print("Result:",result)
              elif(action==0):
                  print("Exit to Operation...")
                  break
              else:
                  print("Invaild Choice !!!")
    elif(choice==0):
        print("Exiting Calculator ....")
        break
    else:
        print("Invaild Choice !!!")

