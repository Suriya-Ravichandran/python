a=['a','b','c']
b=['a','b','c']
z=a
print(z)

if a==b:
    print("same")
else:
    print("not same")

print(id(a))
print(id(b))

if a is z:
    print("same")
else:
    print("not same")