# List of ASCII values
list1 = [65, 66, 67, 68]

# Convert ASCII values to characters and store in a new list
char_list = [chr(i) for i in list1]
print("Character List:", char_list)

# Convert characters back to ASCII values and store in another list
ascii_list = [ord(ch) for ch in char_list]
print("ASCII List:", ascii_list)

list2=[ x  for x in range(10)]
print(list2)

z=int(input("Enter the value: "))
for y in range(z):
    if(y==1):
        print(f"{y} is one")
    print(y)