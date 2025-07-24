ticket=[]

for x in range(5):
    ticket.append(f"Person {x+1}")
print(ticket)

for x in range(len(ticket)):
    del ticket[0]
    print(ticket)