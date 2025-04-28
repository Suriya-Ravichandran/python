data={"foo","goo","boo","zoo"}
print(data)
data2=list(data)
print(data2[0])

for x in data:
    print(x)


data.add("koo")
print(data)

data.remove("koo")
print(data)