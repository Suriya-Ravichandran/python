data1=["foo","boo","goo"]
print(id(data1))
data2=["foo","boo","goo"]
print(id(data2))
data3=data1
print(data1 is not data3)