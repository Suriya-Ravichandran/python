stack=[]
print("Empty Stack")
print(stack)

# push values
for x in range(1,10):
    stack.append(f"Book {x}")

print("Stack With values")
print(stack)

for x in range(len(stack)):
    stack.pop()
    print("Stack Removing")
    print(stack)