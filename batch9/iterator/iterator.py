data={"user1":"foo","user2":"boo","user3":"goo","user4":"zoo"}

# for x in data:
#     print(x)

loop=iter(data)

print(f"User 1: {next(loop)}")
print(f"User 2: {next(loop)}")
print(f"User 3: {next(loop)}")
print(f"User 4: {next(loop)}")