stack=[]
print("Empty stack")
print(stack)

# push values
for x in range(1,10):
    stack.append(x)

print("stack with values")
print(stack)

# pop
for x in range(len(stack)):
    stack.pop()
    print("Stack Removing....")
    print(stack)

