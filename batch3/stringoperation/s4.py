#
text="helloworld"
#     0123456789
#     12345678910

#[index:lenght]
print("-----slicing------")
print(text[2:7])

text2="    helloworld "
print(text2)
print("-----strip-------")
print(text2.strip())

text3="hello,#world"
print("-------split-----")
text3=text3.split(",")
print(text3)
text3=text3[0]+text3[1]
print(text3)
text3=text3.split("#")
print(text3)


