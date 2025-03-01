even=[]
square=[]
for x in range(0,50):
    if x%2==0:
        even.append(x)
print(even)

for x in even:
    data=x*x
    square.append(data)

print(square)