a=[10,20]
b=[10,20]
z=a
print(id(a))
print(id(b))
print(id(z))

print(a is not z)
print(a is not b)
print(z is not a)