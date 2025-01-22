num1=int(input("Enter num 1:"))
num2=int(input("Enter num 2:"))


def add(num1):
    return lambda num2:num2 + num1

result=add(num1)

print(result(num2))
