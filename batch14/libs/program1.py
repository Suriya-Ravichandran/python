import numpy as np

data1=[1,2,3,4,5]
data2=[6,7,8,9,10]


arr=np.array([data1,data2])
print(arr)

print(arr[0][3])
print(arr[1][3])
print(arr[0][3]*arr[1][3])