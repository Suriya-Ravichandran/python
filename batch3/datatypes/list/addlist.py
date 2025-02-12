num=[1,2,3,4,5]

print(num)
# append() add the element in end of list
num.append(6)

print(num)

# to insert a list item at a specified index

num.insert(1,3) #first arg is index second arg is value
num.insert(1,"hello")
print(num)

text=["hello","world","contry"]
num2=[1,2,3,4,5]

text.extend(num2)
print(text)
