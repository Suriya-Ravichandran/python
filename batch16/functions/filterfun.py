def agechecker(age):
    if age>=18:
        return True
    else:
        return False
age=[4,9,10,15,18,25,30,21]

loop=filter(agechecker,age)
print(f"Eligable to vote: {list(loop)}")