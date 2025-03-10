set1=[]
set2=[]

size=int(input("Enter your set 1st size: "))
size2=int(input("Enter your set 2nd size: "))

for x in range(size):
    data=str(input("Enter your 1st set data: "))
    set1.append(data)

for x in range(size2):
    data=str(input("Enter your 2nd set data: "))
    set2.append(data)

set1=set(set1)
set2=set(set2)
print(type(set1))
print("Set 1:",set1)
print("Set 2:",set2)

result=set1.difference(set2)

print("Difference Set:",result)
