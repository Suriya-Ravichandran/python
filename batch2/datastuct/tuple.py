tuple1=(1,2,3,4,5,6)
listtuple=list(tuple1)
listtuple[0]=5
tupleback=tuple(listtuple)
print(type(tupleback))
print(tupleback)


tuple12=(1,2,3)
(one,two,Three)=tuple12
print(one)

for x in range(len(tuple1)):
    print(tuple1[x])

new=tuple1+tuple12
print(new.index(6))
print(new)