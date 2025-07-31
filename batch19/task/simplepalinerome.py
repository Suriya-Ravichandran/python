x=str(input("Enter your word: "))

rev=x[::-1]
if x==rev:
    print(f"Palinerome: {x}")
else:
    print(f"Non Palinerome: {x}")