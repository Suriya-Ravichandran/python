set1={1,1,1,2,2,2,3,3,3}
text={"hello","world","new","new world","contry"}
print(text)

# access set
for x in text:
    print(x)

#add set
text.add("bus")
print(text)
# update set
text2={"car","bike"}
text.update(text2)
print(text)

#remove

text.remove("bike")
print(text)

#discard

text.discard("car")
print(text)

#pop
text.pop()
print(text)

#clear

text.clear()
print(text)