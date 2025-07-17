data={
    "name":"foo",
    "email":"foo@mail.com",
    "age":23,
    "married":True,
    "phoneno":{
        "no1":1234545,
        "no2":12344657
    }
}

print(data["name"])

data["password"]=12345

print(data)
del data["married"]

data["name"]="boo"



print(data)

# for x in data.items():
#     print(x)


print(data["phoneno"]["no1"])