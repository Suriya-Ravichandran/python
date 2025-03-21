student1={
    "name":"foo",
    "age":"24",
    "email":"foo@gmail.com"
}


student1.pop("email")

print(student1)

del student1["age"]
print(student1)

student1.clear()
print(student1)