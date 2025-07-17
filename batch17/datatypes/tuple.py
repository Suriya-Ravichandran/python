data=("apple","orange","graphs","mango")

# print(data[0])

# for x in data:
#     print(x)

# for x in range(len(data)):
#     print(data[x])

# datalist=list(data)
# datalist.append("goa")
# data=tuple(datalist)
# print(data)

# (fruit1,fruit2,)

user=("foo","foo@gmail.com","12345")

(name,email,password)=user

userpassword=str(input("Enter your password: "))
if password==userpassword:
    print("Login success")
    print(name)