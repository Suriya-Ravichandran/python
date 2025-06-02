from module.usermodel import User

u1=User("foo","foo@gmail.com","foo@123")

print(u1.getname())
u1.setname("boo")
print(u1.getname())
print(u1.getemail())
print(u1.getpassword())