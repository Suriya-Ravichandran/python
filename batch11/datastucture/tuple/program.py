data=("Apple","graph","orange","banana","Apple",34,True)

datalist=list(data)
datalist.append("FOO")
data=tuple(datalist)
print(data)


print(data.count("Apple"))

print(data.index("graph"))