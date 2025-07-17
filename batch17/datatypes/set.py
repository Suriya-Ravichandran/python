data={"apple","mango","graphs","pineapple","orange"}
print(data)

data.update(("hello","hello","foo","boo"))
print(data)

data.add("world")
print(data)

data.remove("hello")
print(data)

for x in data:
    print(x)


    