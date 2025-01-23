list1=['A','B','C','D','E']
# for x in range(len(list1)):
#     print(x,list1[x])

list1.append('F')
print(list1)
list1[5]="G"
print(list1)
list1.remove("G")
print(list1)

list4=[1,4,5,7,9,2]
print(list4)
list4.sort(reverse=True)
print(list4)

list5=list1+list4
print(list5)


list2=[]
for x in range(10):
    list2.append(x)
print(list2)


# list3=[]
# while True:
#     print("1 to add\nany key to exit")
#     choice=int(input("Enter choice: "))
#     if choice==1:
#         data=str(input("Enter list Items: "))
#         list3.append(data)
#     else:
#         print("data added end")
#         break

# print(list3)


