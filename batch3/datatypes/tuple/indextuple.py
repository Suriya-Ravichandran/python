text=("car","bike","van","foo","boo")

print(text[1])

text2=list(text)
print(type(text2))
text2[1]="Hello"
text=tuple(text2)
print(type(text))
print(text)