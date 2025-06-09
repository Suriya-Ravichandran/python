data={
    "name":"foo",
    "age":24,
    "email":"foo@gmail.com",

}

print(data["name"])

for x in data.items():
    print(x)

data["email"]="boo@gmail.com"
print(data)

data2=dict(product="apple",price=23)

print(data2)

data.update({"passwor":"123"})
print(data)