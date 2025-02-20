mydict={
    "name" : "foo",
    "Age" : "26",
    "Mark": 499,
    "Email": "foo@gmail.com",
    "Password": "foo@123"
}

print("------keys-------")

for x in mydict:
    print(x)


print("----values------")
for x in mydict:
    print(mydict[x])

print("-------access key function-------")
for x in mydict.keys():
    print(x)

print("-------access values function-------")
for x in mydict.values():
    print(x)

print("-------access items function-------")
for x in mydict.items():
    print(x)