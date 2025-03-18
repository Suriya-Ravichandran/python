data={"hello","world","foo","foo","foo","boo"}

print(data)

data.add("goo")
print(data)
for x in data:
    print(x)

data.remove("boo")

print(data)