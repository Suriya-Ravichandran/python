import numpy as np

data=[1,2,3,4,5]
data2=[6,7,8,9,10]
array=np.array([data,data2])
print(array[0][2]*array[1][3])
print(array.dtype)

# for x in array:
#     print(x)

for x in array:
    for y in x:
        print(y)