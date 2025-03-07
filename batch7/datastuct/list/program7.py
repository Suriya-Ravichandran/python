data=[1,2,3,4]
strdata=["foo","boo"]

result=data+strdata

print(result)

for x in strdata:
    data.append(x)
print(data)