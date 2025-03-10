data=[1,2,3,4,5,6,7,8]
for x in data:
    try:
        print(data[x])
    except:
        print(f"{x}:index out of range")