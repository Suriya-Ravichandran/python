
import random
import string


length = 32
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

password=str(input("Enter your password: "))
saltkey=random_string
changedpassword=saltkey+password+saltkey

print("newpasword: ",changedpassword)
print("Entered password: ",password)
print("saltkey: ",saltkey)
# print("check password: ",password in changedpassword)
# hack=password not in changedpassword
# print("remove password from data:")
# password=hack
# hackpass=f"{saltkey},{password},{saltkey}"
# print(hackpass)

lengthpass=len(password)
result=length+lengthpass
print(result)
print(changedpassword[length:result])
    