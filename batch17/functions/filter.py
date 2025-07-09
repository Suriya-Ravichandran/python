def voter(age):
    if age>=18:
        return True
    else:
        return False
    
def nonvoter(age):
    if age<18:
        return True
    else:
        return False

age=[18,19,60,34,56,78,2,79,11,12,14]

voters=filter(voter,age)
nonvoters=filter(nonvoter,age)
print(f"Voters list: {list(voters)}")
print(f"Non Voters list: {list(nonvoters)}")

