data=(1,2,3,4,5,6,7,3,2,4,2)
print(data)
data2=list(data) # change tuple to list
data2[4]=8 # change the value 
data=tuple(data2) #change list to tuple
print(data)

print(data.count(2))
print(data.index(4))