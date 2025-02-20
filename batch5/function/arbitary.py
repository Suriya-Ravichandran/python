def my_function(*name):
  print("This is " + name[0])

my_function("foo", "boo", "koo")


def key_function(fname,lname,email):
   print(fname,lname,email)

key_function(fname="foo",email="foo@gmail.com",lname="boo")

def double_aribiutary(**name):
   print(name["fname"]+name["lname"])

double_aribiutary(fname="foo",lname="boo")
