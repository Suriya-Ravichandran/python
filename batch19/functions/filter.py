def voter(age):
    if age>=18:
        return True
    else:
        return False
    
data=[12,45,67,34,43,18,19,23,21,35,50,10,8,9,3,4,16]

eligiblevoter=filter(voter,data)
print("Eligible Voter: ",list(eligiblevoter))
