data=["foo","boo","goo"]

loop=iter(data)

for x in range(len(data)):
    print(next(loop))
