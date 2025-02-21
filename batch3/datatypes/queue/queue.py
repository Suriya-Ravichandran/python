queue=[]

for x in range(10):
    queue.append(x)

print("queue is created")
print(queue)

for j in range(len(queue)):
    del queue[0]
    print("Removing Queue")
    print(queue)