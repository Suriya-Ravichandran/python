data={
    "name":"foo",
    "email":"foo@gmail.com",
    "age":60
}

print(data["name"])

data["name"]="boo"
print(data)

data["password"]="foo@123"

print(data)

data.pop("password")
print(data)

del data["age"]
print(data)

data.clear()
print(data)

