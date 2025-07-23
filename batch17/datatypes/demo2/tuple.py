data=("apple","banana","graphs")

print(data[0])

for x in data:
    print(x)

(fruit1,fruit2,fruit3)=data

print(fruit1)

datalist=list(data)
datalist.append("pine apple")
data=tuple(datalist)

strdata="PINEAPPLE"

for x in strdata:
    print(ord(x))
