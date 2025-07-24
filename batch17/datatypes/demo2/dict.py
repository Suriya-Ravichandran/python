# name=str(input("Enter name: "))

data1={
    "name":"foo",
    "email":"foo@gmail.com",
    "passwd":1234
}
print(data1)

data1["name"]="boo"

print(data1)

data1["age"]=34
print(data1)

data1.update(phone=1234567890)
print(data1)
