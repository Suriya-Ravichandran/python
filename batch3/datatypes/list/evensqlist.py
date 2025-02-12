even=[]
result=[]

for x in range(1,11):
    if x%2==0:
        even.append(x)

for x in range(len(even)):
    data=even[x]*even[x]
    print(data)
    result.append(data)
# data=even[0]*even[0]
# result.append(data)
# data=even[1]*even[1]
# result.append(data)
# data=even[2]*even[2]
# result.append(data)
# data=even[3]*even[3]
# result.append(data)
# data=even[4]*even[4]
# result.append(data)


print("Even number List")
print(even)
print("Squared Even Number")
print(result)

print("Finnal square Number:")
print(data)

print(even.count())

# print(len(even))