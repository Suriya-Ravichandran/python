data=("hello","world","foo","foo")
# data[0]="boo"

# print(data)

# for x in data:
#     print(x)

print(data)

data1=list(data)

data1.append("boo")

print(data1)
data=tuple(data1)
print(data)

print(data.index("hello"))

print(data.count("foo"))