list2=["hello","world","hero"]

print("lenth of list: ",len(list2))

i=0

while i<=len(list2):
    try:
       print(list2[i])
    except:
        print("Index out of range")
    i+=1