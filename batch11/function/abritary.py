def name( *args):
    print(args[1])

name("foo","boo","goo","zoo")

def email( **kargs):
    print(kargs)
    print(kargs["foo"])


email(foo="foo@gmail.com",boo="boo@gmail.com")