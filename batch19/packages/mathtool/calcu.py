from .error import Suriyaerror

def add():
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    return num1+num2

def sub():
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    return num1-num2

def mul():
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    return num1*num2

def div():
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    if num1==0 or num2==0:
        raise Suriyaerror("This is my own error")
    else:
        return num1/num2