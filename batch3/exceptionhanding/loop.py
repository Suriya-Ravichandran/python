list1=[1,2,3,4,5,6,7]
list2=["hello","world","hero"]
for x in list1:
    try:
        print(list1[x])
    except:
        print("index out of range")

# for x in range(list1):
#     print(list2[x])