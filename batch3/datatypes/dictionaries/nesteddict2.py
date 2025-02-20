user1={
        "name" : "foo",
        "Age" : "26",
        "Mark": 499,
        "Email": "foo@gmail.com",
        "Password": "foo@123"
     }
user2={
        "name" : "boo",
        "Age" : "26",
        "Mark": 499,
        "Email": "boo@gmail.com",
        "Password": "boo@123"
     }
userdata={
    "user1":user1,
    "user2":user2
}

print(userdata["user1"]["user2"])