import collections 

queue=[]

for x in range(10):
    queue.append(x)

print("Queue Creating.....")
print(queue)


for j in range(len(queue)):
   del queue[0]
   print("Removing Queue....")
   print(queue)
