password = str(input("Enter your password: "))

new_password = password 
for x in range(len(password)):
    if x == len(password) - 1:
        break
    else:
        new_password = new_password.replace(password[x], password[x-1])
print(new_password)
