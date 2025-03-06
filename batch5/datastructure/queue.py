queue=[]

print("-----queue creation------")
for x in range(1,10):
    queue.append(x)
    print(queue)

print("-------clear queue-----")

for x in range(len(queue)):
     del queue[0]
     print(queue)

