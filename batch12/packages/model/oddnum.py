def odd(num):
    oddlist=[]
    for x in range(num):
        if x % 2!=0:
            oddlist.append(x)
    return oddlist