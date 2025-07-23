data=["apple","mango","banana"]

print(data)

print(data[0])

for x in data:
    print(x)
for x in range(len(data)):
    print(data[x])

data[0]="graphs"
print(data)

data.append("apple")
print(data)

data.insert(1,"pine apple")
print(data)


data.pop()
print(data)

data.pop(1)
print(data)

data.remove("banana")
print(data)

del data[1]
print(data)

data.clear()
print(data)

data="hello"
print(data[::-1])