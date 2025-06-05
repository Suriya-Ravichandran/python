# def friuts(values):
#      return values


# data=["apple","banana","graphs"]
# loop=map(friuts,data)
# print(list(loop))

num=[1,2,3,4,5,6,7,8,9,10]

def Even(values):
    if values%2==0:
        return True
    else:
        return False
loop=filter(Even,num)
print(list(loop))


