data=("hello","world","india","world")

print(data[0])

for x in data:
    print(x)

data1=list(data)
print(data1)
data1.append("newworld")
data=tuple(data1)
print(data)

print(data.index("world"))
print(data.count("world"))