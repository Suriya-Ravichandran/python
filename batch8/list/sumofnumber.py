even=[]
sumof=[]
for x in range(1,11):
    if x%2==0:
        even.append(x)

for x in range(3):
    data=even[x]+even[x+2]
    sumof.append(data)

print(even)
print(sumof)

