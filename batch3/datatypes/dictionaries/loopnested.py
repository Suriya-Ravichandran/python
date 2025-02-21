mydict={
    "user1":{
        "name" : "foo",
        "Age" : "26",
        "Mark": 499,
        "Email": "foo@gmail.com",
        "Password": "foo@123"
    },
     "user2":{
        "name" : "boo",
        "Age" : "26",
        "Mark": 499,
        "Email": "boo@gmail.com",
        "Password": "boo@123"
    }
}

for x, y in mydict.items():
    print(x)
    for z in y:
        print(z + ':',y[z])