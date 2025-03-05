# default arguments
def add(value1=30,value2=30):
    return value1+value2

print(add(40,50))

#keyword arguments

def login(username,password):
    print("Username:",username)
    print("password:",password)

login(password=1234,username="foo@mail.com")

# Arbitrary Arguments, *args

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
