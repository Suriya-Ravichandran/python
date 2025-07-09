def square(data):
    return data*data


num=[10,45,20,59,60]

results=map(square,num)

print(list(results))

finnalresult=[]

for x in num:
    result=square(x)
    # print(result)
    finnalresult.append(result)
print(finnalresult)