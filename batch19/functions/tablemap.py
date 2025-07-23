def createtb(num):
    result=num*2
    return result
data=[1,2,3,4,5,6,7,8,9,10]

table=map(createtb,data)
print(list(table))