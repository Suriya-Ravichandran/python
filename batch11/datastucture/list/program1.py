data=["Apple","graph","orange","banana"]

print(len(data))

print(data[0])

print(data)

data.append("stawberry")
print(data)
data.insert(2,"helllo")
print(data)

data.extend(("world","india"))
print(data)

data.remove("india")

print(data)

data.pop()
print(data)

data.pop(1)
print(data)

del data[3]
print(data)

data.clear()
print(data)