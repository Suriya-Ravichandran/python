data=("foo","boo","goo","zoo")

data2=list(data)

# print(data2)

data2.append("hello")

data=tuple(data2)

print(data)

data3=list(data)
data3.remove("hello")
data=tuple(data3)
print(data)