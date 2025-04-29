data={
    "name":"foo",
    "password":"foo@123",
    "email":"foo@gmail.com"
}


# print(data["name"])

# for x in data.items():
#     print(x)

print(data)


data={
    "user1":{
        "name":"foo",
        "password":"foo@123",
    },
    "user2":{
        "name":"boo",
        "password":"boo@123"
    }
}

print(data)
print(data["user2"]["name"])