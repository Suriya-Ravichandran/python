import random

pqueue=[]
random_number = random.randint(1, 5)

for x in range(1,6):
    pqueue.append(x)
   
print("queue:",pqueue)
print("heart attack person:",random_number)
pqueue.remove(random_number)
print(pqueue)


