from .error import MyError


def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2


def mul(num1,num2):
    return num1*num2


def div(num1,num2):
    if num1==0 or num2==0:
        raise MyError("you try to divide value zero")
    return num1/num2

def mod(num1,num2):
    return num1%num2

def square(num):
    return num*num