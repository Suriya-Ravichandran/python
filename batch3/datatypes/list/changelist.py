# num=[1,2,3,4,5]
# print("Old Data:",num)
# num[0]=5
# print("New data:",num)

num=[1,2,3,4,5]
print("Old Data:",num)
for x in range(5):
    num[x]=str(input(f"Enter Replace Data index of {x} : "))

print("New data:",num)

