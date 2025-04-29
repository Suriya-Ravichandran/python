data={"foo","boo","goo","zoo"}
print(data)

for x in data:
    print(x)

print("zoo" in data)

data2=list(data)
data2.append("hello")
data=set(data2)
print(data)

data.add("world")
print(data)

data.remove("world")

print(data)

data.pop()
print(data)

