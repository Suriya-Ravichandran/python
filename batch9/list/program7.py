data1=["foo","boo","goo","zoo","foo"]
data2=["hello","wolrd","India"]

data3=data1+data2

print(data3)

data1.extend(data2)
print(data1)

data4=data1
print(data4)

print(data1.count("foo"))