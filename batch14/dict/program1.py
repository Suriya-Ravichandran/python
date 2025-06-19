data={
    "name":"foo",
    "age":24,
    "email":"foo@gmail.com",
}

print(data)

# data=dict(name="foo",age=20,email="foo@gmail.com")
# print(data)

# print(data["name"])

# for x in data.items():
#     print(x)

data["password"]="foo@123"

print(data)

data["password"]="boo@123"
print(data)

data.pop("password")
print(data)

del data["age"]
print(data)

data.clear()
print(data)