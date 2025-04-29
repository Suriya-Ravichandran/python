person=[]

for x in range(1,6):
    person.append(f"Person {x}")

print(person)

attack_person=set(person)

first_p=attack_person.pop()

print(first_p)