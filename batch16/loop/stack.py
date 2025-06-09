box=[]

numofbooks=int(input("Enter number of books: "))
box=[" "]*numofbooks


for x in range(numofbooks):
    box[x]=f"Book {x+1}"
print("----ADD BOOKS------")
print(box)
print("-----REMOVE BOOKS-----")
for x in range(len(box)):
    del box[-1]
    print(box)
