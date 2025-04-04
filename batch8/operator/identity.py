data1=["car","bike","van"]
data2=data1
data3=["car","bike","van"]

print(id(data1))
print(id(data2))
print(id(data3))

print(data1 is not data2)
print(data1 is data3)
