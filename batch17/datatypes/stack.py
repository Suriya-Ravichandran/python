box=[]
books=int(input("How many books to store in a box: "))
for x in range(books):
    box.append(f"Book {x+1}")
print("-----added books------")
print(box)
print("---------Removed books---------")
for x in range(len(box)):
    box.pop()
    print(box)