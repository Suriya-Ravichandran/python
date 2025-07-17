a={1,2,4,6,8,4,3,6,7,9,0}
b={4,6,8,9,10,56,1,2,4,5}

aub=a.union(b)
print(aub)

bua=b.union(a)

anb=a.intersection(b)
print(anb)

adb=a.difference(b)
print(adb)

bda=b.difference(a)
print(bda)