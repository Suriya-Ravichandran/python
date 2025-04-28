data=("foo","goo","boo")

print(data[1])

data1=list(data)
data1.append("zoo")

data=tuple(data1)
print(data)

(s1,s2,s3,s4)=data

print(s1)

for x in range(len(data)):
    print(data[x])

print(data.index("goo"))