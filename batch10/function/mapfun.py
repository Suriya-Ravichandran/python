data=[1,2,3,4,5,6]

def square(num):
    return num*num

loop=map(square,data)

print(list(loop))