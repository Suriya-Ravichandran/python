even=[]
sumof=[]
for x in range(1,11):
    if x%2==0:
        even.append(x)

print(even)

for x in range(3):
    output=even[x]+even[x+2]
    sumof.append(output)

print(sumof)