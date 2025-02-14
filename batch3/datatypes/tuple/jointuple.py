# join method 1
text=("a","b","c")
num=(1,2,3)
result=text+num
print(result)


# join method 2
#tuple convert to list
listtext=list(text)
listnum=list(num)


for x in listnum:
    print(x)
    listtext.append(x)

print("List Result",type(listtext))
print(listtext)

finnalresult=tuple(listtext)
print("Finnal result",type(finnalresult))
print(finnalresult)
