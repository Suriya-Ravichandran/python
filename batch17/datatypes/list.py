data=["foo","boo","goo","zoo"]

# print(data)
# print(data[0])
# data[3]="hoo"
# print(data)
# print(len(data))

# for x in range(len(data)):
#     print(data[x])

data.append("koo")
print(data)
data.insert(2,"coo")
print(data)
data.reverse()
print(data)

data.pop()
print(data)

popdata=data.pop(3)
print(data)
print(popdata)

data.remove("zoo")
print(data)

del data[1]
print(data)

data.clear()
print(data)
