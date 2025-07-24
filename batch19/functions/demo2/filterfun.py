def voteeligible(age):
    if age>=18:
        return True
    else:
        return False


age=[12,13,45,30,56,36,46,27,23,24,10,7,6,8,9]

result=filter(voteeligible,age)
print("Voters:",list(result))

