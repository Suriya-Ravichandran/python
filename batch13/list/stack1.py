# get user input
HMB=int(input("Enter HMB book: "))
box=[" "]*HMB

#add book in box
for x in range(HMB):
    box[x]=f"Book {x+1}"

print(box)

# find len of box
count=0
for x in box:
    count+=1

# remove the book in lifo
for x in range(count):
    del box[-1]
    print(box)
    