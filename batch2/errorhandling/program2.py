list1=["hello","world","india"]
#          0      1      2

print("len list:",len(list1))


i=0
while i<=len(list1):
    # print(i)
    try: 
        print(list1[i])
        
    except:
        print("Index out of range")
    i+=1
