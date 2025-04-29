person=[]

for x in range(1,6):
    person.append(f"Person {x}")

print(person)

for x in range(len(person)):
    del person[0]
    print(person)

