import numpy as n

array1= n.array([1,2,3,4,5])
array2=n.array([[1,2,3,4],[5,6,7,8]])


print(type(array1))

print(array1)
print(array2)

print(array1[1:4])
new=n.array_split(array1,2)
print(new)

x=n.where(array1==3)
print(x)