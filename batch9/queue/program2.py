pqueue=[]


for x in range(5):
    pqueue.append(f"Person {x+1}")

print(pqueue)
attack=set(pqueue)
p=list(attack)
data=p.pop(0)
print(data)
