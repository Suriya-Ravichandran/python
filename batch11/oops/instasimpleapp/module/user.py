class User():

    def __init__(self,name,email,password,age):
        self.name=name
        self.email=email
        self.password=password
        self.age=age

    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name


# testing

u1=User(name="suriya",email="suriya@gmail.com",password="suriya@123",age=23)

print(u1.getname())

u1.setname("fooo")

print(u1.getname())