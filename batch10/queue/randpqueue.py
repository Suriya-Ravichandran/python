import random

person=[]

for x in range(1,6):
    person.append(f"Person {x}")

print(person)

for x in range(len(person)):
    attack_person=random.randint(0,4)
    first_p=person[attack_person]
print(first_p)