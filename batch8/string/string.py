fname="Suriya"
Lname="Ravichandran"

data="hello,world"

print("Name: "+fname+Lname)
# string methods
print(fname.upper())
print(Lname.lower())
print(Lname.capitalize())
print(fname[2:4])
print(data.split(","))
print(data.replace("h","g"))
print(data[::-1])

for x in Lname:
    print(x)