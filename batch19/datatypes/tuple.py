data=("foo",21,"foo@gmail.com","foo")

print(data[0])

print(data.count("foo"))

print(data.index("foo@gmail.com"))

datalist=list(data)
datalist.append("foo@123")
data=tuple(datalist)
print(data)