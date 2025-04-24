def square(num):
    print(num*num)

data=[2,4,6,8,10]

result=map(square,data)

for x in result:
    print(x)
