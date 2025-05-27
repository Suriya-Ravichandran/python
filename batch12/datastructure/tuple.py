tp=("foo","foo","boo","goo","hoo","koo")

print(tp[0])
print("-----------------------")
for x in tp:
    print(x)
print("-----------------------")
for x in range(len(tp)):
    print(tp[x])


lis=list(tp)
lis.append("zoo")
tp=tuple(lis)
print(tp)

print(tp.count("foo"))

print(tp.index("goo"))

lis=list(tp)
lis.remove("goo")
tp=tuple(lis)
print(tp)


