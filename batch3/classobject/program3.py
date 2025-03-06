from classes.user import User

username=str(input("Enter UserName: "))
password=str(input("Enter Password: "))

u1=User(username,password)

print(u1.user)
print(u1.passwd)