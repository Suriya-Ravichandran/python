import numpy as np

row1=[1,2,3,4,5]
row2=[6,7,8,9,10]

result=np.array([row1,row2])
print(result)
print(type(result))


print(result[0,2]+result[1,3])