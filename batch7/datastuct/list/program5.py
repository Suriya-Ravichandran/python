data=[1,2,3,4,5,6,7,8,9,10]

print(data[2:5]) #


data=[10,20,30,90,80]
result=[]
print(data)
for x in range(3):
    value1=data[x]+data[x+2]
    # value2=data[1]+data[3]
    # value3=data[0]+data[2]
    result.append(value1)

# data=[value1,value2,value3]
print(result)




