def square(*args):
    for x in range(len(args)):
        print(args[x]*args[x])

square(10,30,50,60,25,46,78)

def userdata(**args):
    # print(args)
    for x in args:
        print(args[x])


userdata(name="foo",email="foo@gmail.com",age=24)
