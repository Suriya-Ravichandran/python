data={"foo","foo","boo","boo","hoo"}
print(data)

for x in data:
    print(x)

print("hoo" in data)
data.add("koo")
print(data)

list=["hello","hello","world"]
data.update(list)
print(data)

data.remove("hello")

print(data)

data.pop()

print(data)