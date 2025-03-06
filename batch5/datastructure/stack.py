data=[]

print("----data is adding------")
for x in range(1,10):
    data.append(f"Book {x}")
    print(data)


print("------data is removing------")
for x in range(len(data)):
    del data[len(data)-1]
    print(data)