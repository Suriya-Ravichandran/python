import numpy as np

row1=[1,2,3,4,5]
row2=[6,7,8,9,10]
data=np.array([row1,row2])

result = data[0,2]+data[1,3]
print(result)

