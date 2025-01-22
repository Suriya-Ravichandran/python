Name="Suriya"
Passion="Trainner"
age=30
result=f"Name:{Name} Passion: {Passion} Age: {age}"
print(result)

txt="6400"
print(txt.isdecimal())

txt=["hello","world","this"]
newTxt="Python"
txt.append(newTxt)
for x in txt:
    print(x)

newtxt2=newtxt2= " ".join(txt)
print(newtxt2)
newtxt2=newtxt2.startswith("Hello")
print(newtxt2)

newtxt3="hello world"
x=newtxt3.split()
print(type(x))
x.append("this")
print(x)

newtxt4="Hello$world$this"
x=newtxt4.rsplit("$")
print(x)
