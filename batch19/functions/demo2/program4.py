def userdata(**user):
    print(user)

    print(user["name"])
    print(user["email"])
    print(user["passwd"])


userdata(name="foo",email="foo@gmail.com",passwd="foo@123")
