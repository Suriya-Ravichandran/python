fruits=["mango","orange","apple","banana","straberry"]

# print(f"Yellow: {fruits[0]}, orange: {fruits[1]},Red: {fruits[2]},Green: {fruits[3]},Red: {fruits[4]}")

# for x in fruits:
#     print(x)


# for x in range(len(fruits)):
#     print(fruits[x])

fruits.append("Goa")
print(fruits)

fruits[0]="graphs"
print(fruits)

fruits.insert(2,"mango")
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(1)
print(fruits)

fruits.remove("banana")
print(fruits)

del fruits[0]

print(fruits)

fruits.clear()

print(fruits)

number=[1,2,3,4,5]

number.reverse()
print(number)

number.sort()
print(number)

even=[]
for x in range(11):
    if x%2==0:
        even.append(x)
print(even)