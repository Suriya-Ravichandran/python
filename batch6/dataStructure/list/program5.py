# list creation
even=[]
odd=[]
sum_of_Even_odd=[]

#find even number
for x in range(1,11):
    if x%2==0:
        even.append(x)
    elif x%2!=0:
        odd.append(x)
    else:
        print("invaild number")

# sum of even and odd numbers
for x in range(len(even)):
    sum_of_Even_odd.append(even[x]+odd[x])


# print even, odd and result
print("Even:",even)
print("Odd:",odd)
print("Sumof:",sum_of_Even_odd)