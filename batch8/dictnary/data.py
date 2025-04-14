data={
    "name":"foo",
    "email":"foo@gmail.com",
    "password":"foo@123"
}


print(data.get("email"))

print(data.keys())
print(data.values())
print(data.items())

data["name"]="boo"

print(data)

data.update({"dob":"12-12-2001"})
print(data)

data.pop("dob")
print(data)