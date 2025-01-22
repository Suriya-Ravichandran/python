num=[1,2,3,4,5]

def square(num):
    return num*num

num2=map(square,num)

num3=list(num2)
print(num3)