data={
    "name":"foo",
    "age":28,
    "email":"foo@gmail.com",
    "password":"foo@123"
    }

print(data["name"])

for x in data.values():
    print(x)

for x in data.keys():
    print(x)

for x in data.items():
    print(x)

data["name"]="boo"
print(data)

data["dept"]="BCA"
print(data)