user2={
    "name":"suriya",
    "email":"suriya@gmail.com",
    "password":"suriyapasswd"
}

user2.update({"password":"suriya@123"})
print(user2)

user2["hello"]="world"
print(user2)

user2.pop("hello")
print(user2)

user2.popitem()
print(user2)

user2.clear()
print(user2)

