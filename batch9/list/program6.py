data=["foo","boo","goo","zoo"]

for x in data:
    print(x)

print("--------")

for x in range(len(data)):
    print(data[x])

print("---------")

for x in range(1,11):
    data.append(x)

print(data)