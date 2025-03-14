even=[]
result=[]

# find even number

for x in range(1,11):
    if x%2==0:
        even.append(x)

# add operation performed
for x in range(3):
    result.append(even[x]+even[x+2])


# print lists
print("Even:",even)
print("result:",result)