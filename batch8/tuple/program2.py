data=("foo","boo","suriya")
print(id(data))
x=list(data)
print(x)

x.append("hoo")
print(x)

data=tuple(x)
print(data)
print(id(data))