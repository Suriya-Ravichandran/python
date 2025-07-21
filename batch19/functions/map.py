def square(num):
    return num*num

data=[20,40,50,28,60,79,13,67]

result=map(square,data)
print(list(result))

# for x in data:
#     print(square(x))