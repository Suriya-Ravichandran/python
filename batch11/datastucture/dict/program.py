# data=dict(name="foo",email="foo@gmail.com",age=25)
data={
    "name":"foo",
    "email":"foo@gmail.com",
    "age":25
}
print(data["name"])


for x in data.items():
    print(x)


data.update({"password":"foo@123"})

print(data)