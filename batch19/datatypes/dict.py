#JSON

userdata={
    "name":"foo",
    "age":34,
    "email":"foo@gmail.com",
    "password":"foo@098"
}
print(userdata)
userdata["name"]="boo"
userdata.update({"phone":1234567})

print(userdata)