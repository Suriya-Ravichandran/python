text="Hello world"
print("--------index access------")
print(text[0])
print(text[1])
print(text[2])

print("------using for--------")

for x in text:
    print(x)

print("------using for 2--------")
for x in range(len(text)):
    print(text[x])
